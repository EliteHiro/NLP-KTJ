from groq import Groq

class RAGAgent:
    def __init__(self, retriever):
        self.retriever = retriever
        self.client = Groq()

    def answer(self, query):
        chunks = self.retriever.retrieve(query)
        if not chunks:
            return {"answer": "Not found", "sources": []}

        context = "\n\n".join(
            f"[Page {c['metadata']['page']}]\n{c['text']}"
            for c in chunks
        )

        prompt = f"""
Answer ONLY using the context.

Context:
{context}

Question:
{query}
"""

        res = self.client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        return {
            "answer": res.choices[0].message.content,
            "sources": [{"page": c["metadata"]["page"]} for c in chunks]
        }
