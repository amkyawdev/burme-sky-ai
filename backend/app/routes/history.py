from fastapi import APIRouter, HTTPException
from app.schemas import HistoryItem, HistoryList
from typing import List
import uuid
from datetime import datetime

router = APIRouter()

# In-memory storage (replace with database in production)
history_store: List[HistoryItem] = []


@router.get("/", response_model=HistoryList)
async def get_history():
    """Get all chat history"""
    return HistoryList(history=history_store)


@router.post("/")
async def add_to_history(item: HistoryItem):
    """Add a new history item"""
    item.id = str(uuid.uuid4())
    item.timestamp = datetime.now().isoformat()
    history_store.insert(0, item)
    return item


@router.delete("/{item_id}")
async def delete_history_item(item_id: str):
    """Delete a history item"""
    global history_store
    initial_length = len(history_store)
    history_store = [h for h in history_store if h.id != item_id]
    
    if len(history_store) == initial_length:
        raise HTTPException(status_code=404, detail="History item not found")
    
    return {"message": "Item deleted successfully"}


@router.delete("/")
async def clear_history():
    """Clear all history"""
    global history_store
    history_store = []
    return {"message": "History cleared successfully"}
