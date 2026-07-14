import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat, history, models

app = FastAPI(
    title="Burme Sky AI API",
    description="Backend API for Burme Sky AI Chat Application",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(chat.router, prefix="/api/chat", tags=["chat"])
app.include_router(history.router, prefix="/api/history", tags=["history"])
app.include_router(models.router, prefix="/api/models", tags=["models"])


@app.get("/")
def root():
    return {"status": "Burme Sky AI is running", "version": "1.0.0"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}
