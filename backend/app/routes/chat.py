from fastapi import APIRouter, HTTPException
from fastapi.responses import StreamingResponse
from app.services.ollama_client import OllamaClient
from app.services.cli_service import CLIService
from app.schemas import ChatRequest, ChatResponse
import json

router = APIRouter()
ollama_client = OllamaClient()
cli_service = CLIService()


@router.post("/stream")
async def stream_chat(request: ChatRequest):
    """Stream chat responses from Ollama"""
    async def generate():
        try:
            async for chunk in ollama_client.stream_chat(request.message, request.model):
                if chunk:
                    yield f"data: {json.dumps({'chunk': chunk})}\n\n"
            
            # Check for CLI commands
            if cli_service.is_cli_command(request.message):
                cli_output = await cli_service.execute_command(request.message)
                for line in cli_output.split('\n'):
                    if line.strip():
                        yield f"data: {json.dumps({'chunk': f'\n{line}'})}\n\n"
            
            yield f"data: {json.dumps({'done': True})}\n\n"
            
        except Exception as e:
            error_data = json.dumps({'error': str(e)})
            yield f"data: {error_data}\n\n"
            yield f"data: {json.dumps({'done': True})}\n\n"
    
    return StreamingResponse(generate(), media_type="text/event-stream")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """Non-streaming chat endpoint"""
    try:
        response = await ollama_client.chat(request.message, request.model)
        return ChatResponse(response=response)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
