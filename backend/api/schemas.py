from pydantic import BaseModel, Field
from typing import List, Optional

class ChatRequest(BaseModel):
    message: str
    model: str = "llama2"
    metadata: Optional[dict] = None

class ChatResponse(BaseModel):
    response: str
    model: Optional[str] = None
    done: bool = True

class Model(BaseModel):
    id: str
    name: str
    description: str = ""
    category: str = "General"

class ModelList(BaseModel):
    models: List[Model] = []

class HistoryItem(BaseModel):
    id: Optional[str] = None
    title: str
    messages: List[dict] = []
    timestamp: Optional[str] = None
    model: Optional[str] = None

class HistoryList(BaseModel):
    history: List[HistoryItem] = []
