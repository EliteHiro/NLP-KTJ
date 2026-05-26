import logging
from app.nlp.pdf_loader import PDFLoader
from app.nlp.chunker import Chunker
from app.nlp.embedder import Embedder
from app.nlp.vector_store import VectorStore
from app.nlp.retriever import Retriever
from app.core.config import DATA_DIR

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────
# Singleton: build / load the index ONCE
# ──────────────────────────────────────────────
PDF_PATH = str(DATA_DIR / "Annual-Report-2024-25.pdf")
INDEX_DIR = str(DATA_DIR / "faiss_index")

_embedder = Embedder()
_vector_store = VectorStore(path=INDEX_DIR)

if _vector_store.is_built():
    logger.info("Loading pre-built FAISS index from disk...")
    _vector_store.load()
else:
    logger.info("No index found — building from PDF (one-time)...")
    loader = PDFLoader(PDF_PATH)
    documents = loader.load()
    chunker = Chunker()
    chunks = chunker.chunk_documents(documents)
    embedded_chunks = _embedder.embed_chunks(chunks)
    _vector_store.build(embedded_chunks)
    logger.info("FAISS index built and saved.")

_retriever = Retriever(_vector_store)


def analyze_query(query: str):
    """Search the pre-built index and return results."""
    query_embedding = _embedder.embed_text(query)
    results = _retriever.retrieve(query_embedding, top_k=5)

    # Build a human-readable answer from retrieved chunks
    if results:
        answer_parts = []
        for r in results:
            page = r.get("metadata", {}).get("page", "?")
            answer_parts.append(f"[Page {page}] {r['text'][:300]}")
        answer = "\n\n".join(answer_parts)
    else:
        answer = "No relevant information found in the document."

    return {
        "intent": "document_query",
        "confidence": 0.85,
        "entities": {"matches": str(len(results))},
        "answer": answer,
    }
