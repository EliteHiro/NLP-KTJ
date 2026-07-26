import os
import logging
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from groq import Groq

from app.nlp.pdf_loader import PDFLoader
from app.nlp.chunker import Chunker
from app.core.config import DATA_DIR

logger = logging.getLogger(__name__)

# ──────────────────────────────────────────────────────
# Load PDF → Chunk → Build TF-IDF index  (once at startup)
# ──────────────────────────────────────────────────────
PDF_PATH = str(DATA_DIR / "Annual-Report-2024-25.pdf")

_tfidf_matrix = None
_vectorizer = None
_chunks = []
_groq_client = None

def _initialize_index():
    global _tfidf_matrix, _vectorizer, _chunks, _groq_client
    if _tfidf_matrix is not None:
        return

    logger.info("Loading PDF and building TF-IDF index...")
    _loader = PDFLoader(PDF_PATH)
    _documents = _loader.load()

    _chunker = Chunker(chunk_size=800, chunk_overlap=150)
    _chunks = _chunker.chunk_documents(_documents)
    _chunk_texts = [c["text"] for c in _chunks]

    _vectorizer = TfidfVectorizer(stop_words="english", max_features=10000)
    _tfidf_matrix = _vectorizer.fit_transform(_chunk_texts)
    logger.info(f"TF-IDF index ready: {len(_chunks)} chunks indexed.")

    # ── Groq client ──────────────────────────────────────
    _groq_key = os.environ.get("GROQ_API_KEY", "")
    _groq_client = Groq(api_key=_groq_key) if _groq_key else None


def _retrieve(query: str, top_k: int = 5):
    """Find the top-k most relevant chunks using TF-IDF cosine similarity."""
    query_vec = _vectorizer.transform([query])
    scores = cosine_similarity(query_vec, _tfidf_matrix).flatten()

    # Get top-k indices sorted by score (descending)
    top_indices = scores.argsort()[-top_k:][::-1]
    results = []
    for idx in top_indices:
        if scores[idx] > 0.01:  # filter out irrelevant noise
            results.append({
                "text": _chunks[idx]["text"],
                "metadata": _chunks[idx]["metadata"],
                "score": float(scores[idx]),
            })
    return results


def _generate_answer(query: str, context_chunks) -> str:
    """Use Groq LLM to generate an answer from the retrieved chunks."""
    if not _groq_client:
        # No API key — fall back to returning raw chunks
        parts = []
        for c in context_chunks:
            page = c.get("metadata", {}).get("page", "?")
            parts.append(f"[Page {page}] {c['text'][:400]}")
        return "\n\n".join(parts) if parts else "No relevant information found."

    context = "\n\n".join(
        f"[Page {c['metadata'].get('page', '?')}]\n{c['text']}"
        for c in context_chunks
    )

    prompt = f"""You are a helpful assistant. Answer the user's question using ONLY the context below.
If the context doesn't contain enough information, say so honestly.
Keep your answer clear and concise.

Context:
{context}

Question: {query}

Answer:"""

    try:
        res = _groq_client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024,
            temperature=0.3,
        )
        return res.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Groq API error: {e}")
        # Fall back to raw chunks on error
        parts = []
        for c in context_chunks:
            page = c.get("metadata", {}).get("page", "?")
            parts.append(f"[Page {page}] {c['text'][:400]}")
        return "\n\n".join(parts) if parts else "Error generating answer."


def analyze_query(query: str):
    """Full RAG pipeline: retrieve → generate answer."""
    _initialize_index()
    results = _retrieve(query, top_k=5)

    answer = _generate_answer(query, results)

    return {
        "intent": "document_query",
        "confidence": 0.85,
        "entities": {"matches": str(len(results))},
        "answer": answer,
    }
