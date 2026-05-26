from typing import Optional
from pydantic import BaseModel

class AnalyzeRequest(BaseModel):
    message: str
    model_type: Optional[str] = "gemma"
    model_name: Optional[str] = "gemma3"
    api_key: Optional[str] = None
