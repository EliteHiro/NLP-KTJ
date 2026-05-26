from sentence_transformers import SentenceTransformer

class Embedder:
    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def embed_text(self, text):
        return self.model.encode(text).tolist()

    def embed_texts(self, texts):
        return self.model.encode(texts).tolist()

    def embed_chunks(self, chunks):
        texts = [c["text"] for c in chunks]
        embeddings = self.embed_texts(texts)

        out = []
        for c, e in zip(chunks, embeddings):
            out.append({
                "text": c["text"],
                "metadata": c["metadata"],
                "embedding": e
            })
        return out
