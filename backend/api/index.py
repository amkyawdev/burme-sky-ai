from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chat import router as chat_router
from history import router as history_router
from models import router as models_router

app = FastAPI(
    title="Burme Sky AI API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat_router, prefix="/api/chat")
app.include_router(history_router, prefix="/api/history")
app.include_router(models_router, prefix="/api/models")

@app.get("/")
def root():
    return {"status": "Burme Sky AI is running", "version": "1.0.0"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
