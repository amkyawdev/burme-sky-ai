from fastapi import APIRouter
from schemas import HistoryItem, HistoryList
from typing import List
import uuid
from datetime import datetime

router = APIRouter()
history_store: List[HistoryItem] = []

@router.get("/", response_model=HistoryList)
async def get_history():
    return HistoryList(history=history_store)

@router.post("/")
async def add_to_history(item: HistoryItem):
    item.id = str(uuid.uuid4())
    item.timestamp = datetime.now().isoformat()
    history_store.insert(0, item)
    return item

@router.delete("/")
async def clear_history():
    history_store.clear()
    return {"message": "History cleared"}
