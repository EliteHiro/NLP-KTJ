from pypdf import PdfReader

class PDFLoader:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path

    def load(self):
        reader = PdfReader(self.pdf_path)
        documents = []

        for i, page in enumerate(reader.pages):
            text = page.extract_text() or ""
            if text.strip():
                documents.append({
                    "text": text,
                    "metadata": {"page": i + 1}
                })

        return documents
