import os
from pathlib import Path

# =============================
# Base paths
# =============================
BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

# =============================
# Server config
# =============================
API_HOST = os.getenv("API_HOST", "0.0.0.0")
API_PORT = int(os.getenv("API_PORT", 8000))
DEBUG = os.getenv("DEBUG", "true").lower() == "true"

# =============================
# Model / NLP config
# =============================
DEFAULT_MODEL_TYPE = os.getenv("DEFAULT_MODEL_TYPE", "gemma")
DEFAULT_OLLAMA_MODEL = os.getenv("DEFAULT_OLLAMA_MODEL", "gemma3")

# Embedding model (used in embedder.py)
EMBEDDING_MODEL_NAME = os.getenv(
    "EMBEDDING_MODEL_NAME",
    "sentence-transformers/all-MiniLM-L6-v2"
)

# =============================
# RAG config
# =============================
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP", 100))

TOP_K_RETRIEVAL = int(os.getenv("TOP_K_RETRIEVAL", 4))

# =============================
# Files
# =============================
PDF_PATH = os.getenv(
    "PDF_PATH",
    str(DATA_DIR / "Annual-Report-2024-25.pdf")
)

# =============================
# Vector store
# =============================
VECTOR_STORE_PATH = os.getenv(
    "VECTOR_STORE_PATH",
    str(DATA_DIR / "vector_store")
)
