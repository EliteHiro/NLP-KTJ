from pydantic import BaseModel
from typing import Dict, Optional

class AnalyzeResponse(BaseModel):
    intent: str
    confidence: float
    entities: Dict[str, str]
    answer: Optional[str] = None
