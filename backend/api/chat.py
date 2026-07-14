from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from services.ollama_client import OllamaClient
from schemas import ChatRequest, ChatResponse
import json

router = APIRouter()
ollama_client = OllamaClient()


@router.post("/stream")
async def stream_chat(request: ChatRequest):
    async def generate():
        try:
            async for chunk in ollama_client.stream_chat(request.message, request.model):
                if chunk:
                    yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
        except Exception as e:
            yield f"data: {json.dumps({'error': str(e)})}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"

    return StreamingResponse(generate(), media_type="text/event-stream")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    try:
        response = await ollama_client.chat(request.message, request.model)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
