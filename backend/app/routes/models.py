from fastapi import APIRouter, HTTPException
from app.schemas import Model, ModelList
import httpx
import os

router = APIRouter()

# Default available models
DEFAULT_MODELS = [
    Model(id="llama2", name="Llama 2", description="General purpose model", category="General"),
    Model(id="codellama", name="Code Llama", description="Code generation model", category="Coding"),
    Model(id="mistral", name="Mistral", description="Fast and efficient", category="Fast"),
    Model(id="mixtral", name="Mixtral", description="High quality responses", category="Quality"),
    Model(id="llama3", name="Llama 3", description="Latest general purpose model", category="General"),
]


@router.get("/", response_model=ModelList)
async def get_models():
    """Get available Ollama models"""
    base_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    
    try:
        async with httpx.AsyncClient(timeout=5.0) as client:
            response = await client.get(f"{base_url}/api/tags")
            
            if response.status_code == 200:
                data = response.json()
                models = [
                    Model(
                        id=m.get("name", "unknown"),
                        name=m.get("name", "Unknown Model"),
                        description=f"Model: {m.get('name', 'unknown')}",
                        category="Loaded"
                    )
                    for m in data.get("models", [])
                ]
                return ModelList(models=models if models else DEFAULT_MODELS)
            
    except Exception as e:
        pass
    
    # Return default models if Ollama is not available
    return ModelList(models=DEFAULT_MODELS)


@router.get("/{model_id}")
async def get_model(model_id: str):
    """Get specific model info"""
    models = await get_models()
    
    for model in models.models:
        if model.id == model_id:
            return model
    
    raise HTTPException(status_code=404, detail="Model not found")
