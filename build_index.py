from pdf_loader import PDFLoader
from chunker import Chunker
from embedder import Embedder
from vector_store import VectorStoreManager

loader = PDFLoader("pdf/Annual-Report-2024-25.pdf")
docs = loader.load()

chunker = Chunker()
chunks = chunker.chunk_documents(docs)

embedder = Embedder()
embedded = embedder.embed_chunks(chunks)

store = VectorStoreManager()
store.build(embedded)

print("FAISS index built")
