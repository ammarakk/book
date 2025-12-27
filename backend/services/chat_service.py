"""
Service for handling chat interactions and RAG pipeline
"""
import asyncio
import logging
from typing import List, Optional, Dict, Any
from datetime import datetime

from models.chat import ChatQuery, ChatResponse, ChatSession
from models.embeddings import DocumentChunk
from services.document_service import DocumentService
from services.embedding_service import EmbeddingService
from config import settings


logger = logging.getLogger(__name__)


class ChatService:
    """
    Service class for handling chat interactions and RAG pipeline
    """
    
    def __init__(self, 
                 document_service: DocumentService, 
                 embedding_service: EmbeddingService):
        self.document_service = document_service
        self.embedding_service = embedding_service

    async def process_query(self, 
                           query: ChatQuery, 
                           session: Optional[ChatSession] = None) -> ChatResponse:
        """
        Process a user query and return a response using the RAG pipeline
        """
        try:
            # Generate embedding for the query
            query_embedding = await self.embedding_service.generate_embedding(query.question_text)
            
            # Determine context mode and retrieve relevant chunks
            relevant_chunks: List[DocumentChunk] = []
            
            if query.context_mode == "global":
                # Search across the entire book content
                relevant_chunks = await self.embedding_service.search_similar(
                    query_embedding=query_embedding,
                    top_k=5  # Retrieve top 5 most relevant chunks
                )
            elif query.context_mode == "selection" and query.selected_text:
                # Search only within the selected text
                selected_text_embedding = await self.embedding_service.generate_embedding(query.selected_text)
                
                # For selection mode, we'll search for chunks similar to the selected text
                # and then ensure the answer comes only from those chunks
                relevant_chunks = await self.embedding_service.search_similar(
                    query_embedding=selected_text_embedding,
                    top_k=5,
                    filters={"source_module": query.selected_text[:50]}  # This is a simplified filter
                )
            else:
                # Default to global search if no specific context mode
                relevant_chunks = await self.embedding_service.search_similar(
                    query_embedding=query_embedding,
                    top_k=5
                )
            
            # Construct the context for the LLM from the relevant chunks
            context = self._construct_context_from_chunks(relevant_chunks)
            
            # Generate the response using the LLM
            answer = await self._generate_answer_with_ollama(
                question=query.question_text,
                context=context,
                context_mode=query.context_mode
            )
            
            # Calculate confidence based on similarity scores and other factors
            confidence = self._calculate_confidence(relevant_chunks, answer)
            
            # Create and return the response
            response = ChatResponse(
                query_id=query.id,
                answer_text=answer,
                source_chunks=[chunk.id for chunk in relevant_chunks],
                confidence_level=confidence,
                retrieval_metadata={
                    "num_chunks_used": len(relevant_chunks),
                    "context_mode": query.context_mode
                },
                timestamp=datetime.utcnow()
            )
            
            logger.info(f"Processed query '{query.question_text[:30]}...' with confidence {confidence}")
            return response
        except Exception as e:
            logger.error(f"Error processing query '{query.question_text[:30]}...': {e}")
            
            # Return a fallback response if processing fails
            return ChatResponse(
                query_id=query.id,
                answer_text="This information is not available in the book.",
                source_chunks=[],
                confidence_level=0.0,
                retrieval_metadata={
                    "error": str(e),
                    "context_mode": query.context_mode
                },
                timestamp=datetime.utcnow()
            )

    def _construct_context_from_chunks(self, chunks: List[DocumentChunk]) -> str:
        """
        Construct a context string from the relevant document chunks
        """
        if not chunks:
            return ""
        
        context_parts = []
        for chunk in chunks:
            context_parts.append(f"Source: {chunk.source_module}/{chunk.source_chapter}/{chunk.source_section}\n")
            context_parts.append(f"Content: {chunk.content}\n")
            context_parts.append("---\n")
        
        return "".join(context_parts)

    async def _generate_answer_with_ollama(self, 
                                         question: str, 
                                         context: str, 
                                         context_mode: str) -> str:
        """
        Generate an answer using the Ollama LLM with the provided context
        """
        import aiohttp
        from aiohttp import ClientSession
        
        # Construct the prompt for the LLM
        if context_mode == "selection":
            system_prompt = (
                "You are an assistant for the Physical AI & Humanoid Robotics book. "
                "You may ONLY answer from the provided context. "
                "If the answer is not in the provided context, respond with: "
                "'This information is not available in the book.'"
                "\n\n"
                "The user has selected specific text and asked a question about it. "
                "Answer ONLY based on the provided context from the selected text."
            )
        else:
            system_prompt = (
                "You are an assistant for the Physical AI & Humanoid Robotics book. "
                "You may ONLY answer from the provided context. "
                "If the answer is not in the provided context, respond with: "
                "'This information is not available in the book.'"
            )
        
        prompt = (
            f"{system_prompt}\n\n"
            f"Context:\n{context}\n\n"
            f"Question: {question}\n\n"
            f"Answer:"
        )
        
        # Prepare the request to Ollama
        ollama_request = {
            "model": settings.OLLAMA_MODEL,
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.1,  # Low temperature for more consistent, factual responses
                "top_p": 0.9
            }
        }
        
        try:
            # Make the request to Ollama
            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{settings.OLLAMA_BASE_URL}/api/generate",
                    json=ollama_request
                ) as response:
                    if response.status == 200:
                        result = await response.json()
                        answer = result.get("response", "").strip()
                        
                        # Ensure the answer follows the rules
                        if not answer or "not available in the book" in answer.lower():
                            return "This information is not available in the book."
                        
                        return answer
                    else:
                        logger.error(f"Ollama request failed with status {response.status}")
                        return "This information is not available in the book."
        except Exception as e:
            logger.error(f"Error calling Ollama: {e}")
            return "This information is not available in the book."

    def _calculate_confidence(self, chunks: List[DocumentChunk], answer: str) -> float:
        """
        Calculate a confidence score based on the relevance of retrieved chunks and answer quality
        """
        if not chunks:
            return 0.0
        
        # Simple confidence calculation based on number of chunks and content match
        # In a more sophisticated implementation, we would use the similarity scores
        # from the vector search and other factors
        
        # Base confidence on number of chunks used (more chunks = higher confidence, up to a point)
        num_chunks_factor = min(len(chunks) / 5.0, 1.0)  # Max contribution of 1.0 from 5+ chunks
        
        # Factor in answer length (very short answers might be less confident)
        answer_length_factor = min(len(answer) / 100.0, 0.5)  # Max contribution of 0.5 from 100+ char answers
        
        # Combine factors
        confidence = (num_chunks_factor * 0.7) + (answer_length_factor * 0.3)
        
        return min(confidence, 1.0)  # Ensure confidence is between 0 and 1

    async def create_chat_session(self, user_id: Optional[str] = None) -> ChatSession:
        """
        Create a new chat session
        """
        session = ChatSession(
            id=f"session_{int(datetime.utcnow().timestamp())}_{user_id or 'anonymous'}",
            user_id=user_id,
            created_at=datetime.utcnow(),
            last_activity_at=datetime.utcnow(),
            is_active=True
        )
        
        return session

    async def get_chat_history(self, session_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve the chat history for a session
        """
        # In a real implementation, this would query the database for chat history
        # For now, returning an empty list as a placeholder
        return []