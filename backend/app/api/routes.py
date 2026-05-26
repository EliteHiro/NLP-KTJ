from fastapi import APIRouter
from app.schemas.request import AnalyzeRequest
from app.schemas.response import AnalyzeResponse
from app.nlp.rag_pipeline import analyze_query

router = APIRouter()

@router.post("/analyze", response_model=AnalyzeResponse)
def analyze(req: AnalyzeRequest):
    return analyze_query(req.message)

@router.get("/config")
def config():
    return {
        "llm": {"default_model": "gemma"},
        "ollama": {"model_name": "gemma3"},
        "gemini": {"model_name": "", "api_key": ""}
    }
