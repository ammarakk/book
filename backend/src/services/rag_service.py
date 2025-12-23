from sqlalchemy.orm import Session
from typing import List
from src.models.book_content import BookContent
from src.config import settings
from qdrant_client import QdrantClient
from qdrant_client.http import models


class RagService:
    """
    Service to handle Retrieval Augmented Generation (RAG) functionality.
    """
    
    def __init__(self, db: Session):
        self.db = db
        self.qdrant_client = QdrantClient(
            url=settings.QDRANT_URL,
            api_key=settings.QDRANT_API_KEY
        )
        self.collection_name = "book_content_embeddings"
    
    def get_relevant_content(self, query: str) -> str:
        """
        Retrieve relevant content based on the query using vector search.
        """
        try:
            # Search for similar content in the vector database
            search_results = self.qdrant_client.search(
                collection_name=self.collection_name,
                query_text=query,
                limit=5  # Get top 5 most relevant results
            )
            
            # Extract and combine the relevant content
            relevant_content = []
            for result in search_results:
                content_id = result.payload.get("content_id")
                content = self.db.query(BookContent).filter(BookContent.id == content_id).first()
                if content:
                    relevant_content.append(content.content)
            
            return "\n\n".join(relevant_content)
        except Exception as e:
            print(f"Error in RAG search: {str(e)}")
            return ""
    
    def get_content_by_chapter(self, chapter_id: int) -> str:
        """
        Retrieve content for a specific chapter.
        """
        chapter = self.db.query(BookContent).filter(BookContent.id == chapter_id).first()
        if chapter:
            return chapter.content
        return ""
    
    def index_content(self, content_id: int, content: str):
        """
        Index content in the vector database for future retrieval.
        """
        try:
            # Create embedding for the content
            # Note: In a real implementation, you would use an embedding model
            # For now, we'll use a placeholder approach
            
            # Upsert the content into Qdrant
            self.qdrant_client.upsert(
                collection_name=self.collection_name,
                points=[
                    models.PointStruct(
                        id=content_id,
                        vector=[0.0] * 384,  # Placeholder vector - in reality, this would be a real embedding
                        payload={
                            "content_id": content_id,
                            "content": content
                        }
                    )
                ]
            )
        except Exception as e:
            print(f"Error indexing content: {str(e)}")