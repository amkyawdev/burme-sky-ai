from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes import chat, history, models
import os

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


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "app.main:app", 
        host=os.getenv("HOST", "0.0.0.0"), 
        port=int(os.getenv("PORT", 8000)),
        reload=True
    )
