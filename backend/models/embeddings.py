from pydantic import BaseModel
from typing import List, Optional, Dict, Any
from datetime import datetime


class VectorEmbedding(BaseModel):
    """
    Numerical representation of document content for similarity matching
    """
    id: str
    document_chunk_id: str
    embedding_vector: List[float]
    created_at: datetime


class DocumentChunk(BaseModel):
    """
    A segment of book content that has been processed for vector storage
    """
    id: str
    content: str
    source_module: str
    source_chapter: str
    source_section: str
    source_url: str
    embedding_id: str
    metadata: Optional[Dict[str, Any]] = None


class EmbeddingRequest(BaseModel):
    """
    Request to generate embeddings for content
    """
    content: str
    document_id: str


class EmbeddingResponse(BaseModel):
    """
    Response with generated embeddings
    """
    embedding: List[float]
    document_id: str
    chunk_id: str