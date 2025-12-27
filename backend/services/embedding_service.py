"""
Service for handling embedding generation and management for the RAG system
"""
import asyncio
from typing import List, Optional
from sentence_transformers import SentenceTransformer
import numpy as np
import logging
from qdrant_client import QdrantClient
from qdrant_client.http.models import PointStruct, VectorParams, Distance

from models.embeddings import VectorEmbedding, DocumentChunk, EmbeddingRequest, EmbeddingResponse
from config import settings


logger = logging.getLogger(__name__)


class EmbeddingService:
    """
    Service class for generating and managing embeddings
    """
    
    def __init__(self):
        # Initialize the sentence transformer model for embedding generation
        self.model = SentenceTransformer('all-MiniLM-L6-v2')  # Using a lightweight model for initial implementation
        # In production, we might want to use a more sophisticated model
        
        # Initialize Qdrant client
        self.qdrant_client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY,
            prefer_grpc=True
        )
        
        # Create collection if it doesn't exist
        self._ensure_collection_exists()

    def _ensure_collection_exists(self):
        """
        Ensure the required Qdrant collection exists
        """
        try:
            collections = self.qdrant_client.get_collections()
            collection_names = [c.name for c in collections.collections]
            
            if "book_embeddings" not in collection_names:
                # Create the collection with appropriate settings
                self.qdrant_client.recreate_collection(
                    collection_name="book_embeddings",
                    vectors_config=VectorParams(size=384, distance=Distance.COSINE),  # 384 is the size for all-MiniLM-L6-v2
                )
                
                logger.info("Created Qdrant collection 'book_embeddings'")
            else:
                logger.info("Qdrant collection 'book_embeddings' already exists")
        except Exception as e:
            logger.error(f"Error ensuring Qdrant collection exists: {e}")

    async def generate_embedding(self, text: str) -> List[float]:
        """
        Generate an embedding for the given text
        """
        loop = asyncio.get_event_loop()
        embedding = await loop.run_in_executor(None, lambda: self.model.encode(text))
        return embedding.tolist()

    async def generate_embeddings_batch(self, texts: List[str]) -> List[List[float]]:
        """
        Generate embeddings for a batch of texts
        """
        loop = asyncio.get_event_loop()
        embeddings = await loop.run_in_executor(None, lambda: self.model.encode(texts))
        return [embedding.tolist() for embedding in embeddings]

    async def store_embedding(self, 
                            document_chunk: DocumentChunk, 
                            embedding: List[float]) -> str:
        """
        Store an embedding in the Qdrant vector database
        """
        try:
            # Create a unique ID for this embedding point
            point_id = document_chunk.id
            
            # Prepare the payload with document metadata
            payload = {
                "document_chunk_id": document_chunk.id,
                "source_module": document_chunk.source_module,
                "source_chapter": document_chunk.source_chapter,
                "source_section": document_chunk.source_section,
                "source_url": document_chunk.source_url
            }
            
            # Store the embedding in Qdrant
            points = [PointStruct(
                id=point_id,
                vector=embedding,
                payload=payload
            )]
            
            self.qdrant_client.upload_points(
                collection_name="book_embeddings",
                points=points
            )
            
            logger.info(f"Stored embedding for document chunk: {document_chunk.id}")
            return point_id
        except Exception as e:
            logger.error(f"Error storing embedding for document chunk {document_chunk.id}: {e}")
            raise

    async def search_similar(self, 
                           query_embedding: List[float], 
                           top_k: int = 5, 
                           filters: Optional[dict] = None) -> List[DocumentChunk]:
        """
        Search for similar document chunks based on the query embedding
        """
        try:
            # Prepare filters if provided
            search_filter = None
            if filters:
                from qdrant_client.http.models import FieldCondition, MatchValue
                conditions = []
                for key, value in filters.items():
                    conditions.append(FieldCondition(key=key, match=MatchValue(value=value)))
                
                if conditions:
                    from qdrant_client.http.models import Filter
                    search_filter = Filter(must=conditions)
            
            # Perform the search
            search_results = self.qdrant_client.search(
                collection_name="book_embeddings",
                query_vector=query_embedding,
                limit=top_k,
                query_filter=search_filter
            )
            
            # Convert results to DocumentChunk objects
            results = []
            for hit in search_results:
                payload = hit.payload
                chunk = DocumentChunk(
                    id=payload.get("document_chunk_id"),
                    content="",  # Content would need to be retrieved separately
                    source_module=payload.get("source_module", ""),
                    source_chapter=payload.get("source_chapter", ""),
                    source_section=payload.get("source_section", ""),
                    source_url=payload.get("source_url", ""),
                    embedding_id=hit.id,
                    metadata=payload
                )
                results.append(chunk)
            
            logger.info(f"Found {len(results)} similar document chunks")
            return results
        except Exception as e:
            logger.error(f"Error searching for similar embeddings: {e}")
            raise

    async def process_document_chunk(self, document_chunk: DocumentChunk) -> str:
        """
        Process a document chunk by generating and storing its embedding
        """
        try:
            # Generate embedding for the document chunk content
            embedding = await self.generate_embedding(document_chunk.content)
            
            # Store the embedding in Qdrant
            embedding_id = await self.store_embedding(document_chunk, embedding)
            
            # Update the document chunk with the embedding ID
            document_chunk.embedding_id = embedding_id
            
            return embedding_id
        except Exception as e:
            logger.error(f"Error processing document chunk {document_chunk.id}: {e}")
            raise

    async def batch_process_document_chunks(self, document_chunks: List[DocumentChunk]) -> List[str]:
        """
        Process multiple document chunks by generating and storing their embeddings
        """
        try:
            # Extract content from all chunks
            contents = [chunk.content for chunk in document_chunks]
            
            # Generate embeddings for all contents in a batch
            embeddings = await self.generate_embeddings_batch(contents)
            
            # Store each embedding and collect the IDs
            embedding_ids = []
            for chunk, embedding in zip(document_chunks, embeddings):
                embedding_id = await self.store_embedding(chunk, embedding)
                chunk.embedding_id = embedding_id
                embedding_ids.append(embedding_id)
            
            logger.info(f"Processed {len(document_chunks)} document chunks in batch")
            return embedding_ids
        except Exception as e:
            logger.error(f"Error processing document chunks in batch: {e}")
            raise