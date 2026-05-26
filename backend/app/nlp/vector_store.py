import faiss
import numpy as np
import os
import pickle

class VectorStore:
    def __init__(self, path="data/faiss_index"):
        self.path = path
        os.makedirs(path, exist_ok=True)
        self.index_file = f"{path}/index.faiss"
        self.meta_file = f"{path}/meta.pkl"
        self.index = None
        self.chunks = None

    def build(self, chunks):
        vectors = np.array([c["embedding"] for c in chunks]).astype("float32")
        self.index = faiss.IndexFlatL2(vectors.shape[1])
        self.index.add(vectors)
        self.chunks = chunks  # Keep in memory so search() works immediately

        with open(self.meta_file, "wb") as f:
            pickle.dump(chunks, f)
        faiss.write_index(self.index, self.index_file)

    def is_built(self):
        """Check if a pre-built index exists on disk."""
        return os.path.exists(self.index_file) and os.path.exists(self.meta_file)

    def load(self):
        self.index = faiss.read_index(self.index_file)
        with open(self.meta_file, "rb") as f:
            self.chunks = pickle.load(f)

    def search(self, query_embedding, top_k=5):
        D, I = self.index.search(
            np.array([query_embedding]).astype("float32"), top_k
        )
        return [self.chunks[i] for i in I[0]]
