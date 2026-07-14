from fastapi import APIRouter
from schemas import Model, ModelList

router = APIRouter()

DEFAULT_MODELS = [
    Model(id="minimax-m2.5", name="MiniMax-M2.5", description="MiniMax model 2.5"),
    Model(id="minimax-m3", name="MiniMax-M3", description="MiniMax model 3"),
    Model(id="ministral-3:8b", name="Ministral-3:8b", description="Ministral 8B model"),
    Model(id="ministral-3:14b", name="Ministral-3:14b", description="Ministral 14B model"),
    Model(id="nemotron-3-nano:30b", name="Nemotron-3:30b", description="Nemotron 30B model"),
]

@router.get("/", response_model=ModelList)
async def get_models():
    return ModelList(models=DEFAULT_MODELS)
