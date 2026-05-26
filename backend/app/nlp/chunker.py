from typing import List, Dict, Any, Optional
import logging
from langchain.text_splitter import RecursiveCharacterTextSplitter

logger = logging.getLogger(__name__)

class Chunker:
    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
        separators: Optional[List[str]] = None
    ):
        """
        Initialize the text chunker.
        
        Args:
            chunk_size: Maximum size of chunks (in characters)
            chunk_overlap: Overlap between chunks (in characters)
            separators: List of separators to use for splitting
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        
        if separators is None:
            separators = ["\n\n", "\n", ". ", " ", ""]
        
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            separators=separators,
            length_function=len,
            is_separator_regex=False,
        )
    
    def chunk_text(
        self,
        text: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Chunk a single text document.
        
        Args:
            text: The text to chunk
            metadata: Optional metadata to attach to each chunk
            
        Returns:
            List of chunks with metadata
        """
        if metadata is None:
            metadata = {}
        
        # Split the text
        chunks = self.text_splitter.split_text(text)
        
        # Create chunk documents with metadata
        chunk_documents = []
        for i, chunk in enumerate(chunks):
            chunk_metadata = metadata.copy()
            chunk_metadata.update({
                "chunk_index": i,
                "total_chunks": len(chunks),
                "chunk_size": len(chunk),
            })
            
            chunk_documents.append({
                "text": chunk,
                "metadata": chunk_metadata
            })
        
        logger.info(f"Chunked text into {len(chunk_documents)} chunks")
        return chunk_documents
    
    def chunk_documents(self, documents: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        all_chunks = []

        for doc_idx, document in enumerate(documents):
            text = document.get("text", "")
            base_metadata = document.get("metadata", {}).copy()

            base_metadata.update({
                "document_index": doc_idx,
                "total_documents": len(documents),
            })

            chunks = self.chunk_text(text, base_metadata)
            all_chunks.extend(chunks)

        logger.info(f"Total chunks created: {len(all_chunks)}")
        return all_chunks

    
    def chunk_by_semantic_units(
        self,
        text: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> List[Dict[str, Any]]:
        """
        Advanced chunking that attempts to preserve semantic units.
        Tries to keep paragraphs, sentences, and logical sections together.
        
        Args:
            text: The text to chunk
            metadata: Optional metadata
            
        Returns:
            List of semantically-aware chunks
        """
        if metadata is None:
            metadata = {}
        
        # First split by double newlines (paragraphs)
        paragraphs = text.split("\n\n")
        
        chunks = []
        current_chunk = ""
        chunk_metadata = metadata.copy()
        
        for para_idx, paragraph in enumerate(paragraphs):
            paragraph = paragraph.strip()
            if not paragraph:
                continue
            
            # Check if adding this paragraph would exceed chunk size
            if len(current_chunk) + len(paragraph) + 2 <= self.chunk_size:
                # Add paragraph to current chunk
                if current_chunk:
                    current_chunk += "\n\n" + paragraph
                else:
                    current_chunk = paragraph
            else:
                # Save current chunk and start new one
                if current_chunk:
                    chunk_metadata.update({
                        "chunk_type": "paragraph_group",
                        "paragraph_count": para_idx,
                    })
                    chunks.append({
                        "text": current_chunk,
                        "metadata": chunk_metadata.copy()
                    })
                
                # Start new chunk with current paragraph
                current_chunk = paragraph
                chunk_metadata = metadata.copy()
        
        # Don't forget the last chunk
        if current_chunk:
            chunk_metadata.update({
                "chunk_type": "paragraph_group",
                "paragraph_count": len(paragraphs),
            })
            chunks.append({
                "text": current_chunk,
                "metadata": chunk_metadata
            })
        
        # If chunks are still too large, recursively split them
        final_chunks = []
        for chunk in chunks:
            if len(chunk["text"]) > self.chunk_size * 1.5:
                # Split this chunk further
                sub_chunks = self.chunk_text(chunk["text"], chunk["metadata"])
                final_chunks.extend(sub_chunks)
            else:
                final_chunks.append(chunk)
        
        logger.info(f"Created {len(final_chunks)} semantic chunks")
        return final_chunks