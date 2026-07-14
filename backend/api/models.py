from fastapi import APIRouter
from schemas import Model, ModelList

router = APIRouter()

DEFAULT_MODELS = [
    Model(id="llama2", name="Llama 2", description="General purpose model"),
    Model(id="codellama", name="Code Llama", description="Code generation"),
    Model(id="mistral", name="Mistral", description="Fast and efficient"),
]

@router.get("/", response_model=ModelList)
async def get_models():
    return ModelList(models=DEFAULT_MODELS)
