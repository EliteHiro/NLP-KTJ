from typing import List, Dict, Any, Optional
import logging

logger = logging.getLogger(__name__)


class Chunker:
    """Pure-Python text chunker — no langchain dependency."""

    def __init__(
        self,
        chunk_size: int = 1000,
        chunk_overlap: int = 200,
    ):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    # ── core split ──────────────────────────────────
    def _split_text(self, text: str) -> List[str]:
        """Split text into overlapping chunks."""
        chunks: List[str] = []
        start = 0
        while start < len(text):
            end = start + self.chunk_size

            # Try to break at a paragraph, then sentence, then space
            if end < len(text):
                for sep in ["\n\n", "\n", ". ", " "]:
                    pos = text.rfind(sep, start, end)
                    if pos > start:
                        end = pos + len(sep)
                        break

            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)

            # Move forward by (chunk_size - overlap)
            start = max(start + 1, end - self.chunk_overlap)

        return chunks

    # ── public API (unchanged interface) ────────────
    def chunk_text(
        self,
        text: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> List[Dict[str, Any]]:
        if metadata is None:
            metadata = {}

        chunks = self._split_text(text)

        chunk_documents = []
        for i, chunk in enumerate(chunks):
            chunk_metadata = metadata.copy()
            chunk_metadata.update({
                "chunk_index": i,
                "total_chunks": len(chunks),
                "chunk_size": len(chunk),
            })
            chunk_documents.append({"text": chunk, "metadata": chunk_metadata})

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