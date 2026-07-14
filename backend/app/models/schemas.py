from pydantic import BaseModel, Field
from typing import List, Optional, Any


class ChatRequest(BaseModel):
    message: str = Field(..., description="The user's message")
    model: str = Field(default="llama2", description="The model to use")
    metadata: Optional[dict] = Field(default=None, description="Optional metadata")


class ChatResponse(BaseModel):
    response: str = Field(..., description="The AI's response")
    model: Optional[str] = Field(default=None, description="Model used")
    done: bool = Field(default=True, description="Whether the response is complete")


class Model(BaseModel):
    id: str = Field(..., description="Model identifier")
    name: str = Field(..., description="Display name")
    description: str = Field(default="", description="Model description")
    category: str = Field(default="General", description="Model category")


class ModelList(BaseModel):
    models: List[Model] = Field(default_factory=list, description="List of available models")


class HistoryItem(BaseModel):
    id: Optional[str] = Field(default=None, description="Unique identifier")
    title: str = Field(..., description="Chat title")
    messages: List[dict] = Field(default_factory=list, description="Chat messages")
    timestamp: Optional[str] = Field(default=None, description="Creation timestamp")
    model: Optional[str] = Field(default=None, description="Model used")


class HistoryList(BaseModel):
    history: List[HistoryItem] = Field(default_factory=list, description="List of history items")


class ErrorResponse(BaseModel):
    error: str = Field(..., description="Error message")
    detail: Optional[str] = Field(default=None, description="Error details")
