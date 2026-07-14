import os
import httpx
from typing import AsyncGenerator


class OllamaClient:
    def __init__(self):
        self.api_key = os.getenv("OLLAMA_API_KEY", "") or os.getenv("OLLAMA_API_KEY_1", "")
        self.base_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
    
    async def stream_chat(self, message: str, model: str = "llama2") -> AsyncGenerator[str, None]:
        """Stream chat responses from Ollama"""
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            try:
                async with client.stream(
                    "POST",
                    f"{self.base_url}/api/generate",
                    json={
                        "model": model, 
                        "prompt": message, 
                        "stream": True,
                        "options": {
                            "temperature": 0.7,
                            "top_p": 0.9,
                            "num_predict": 2048
                        }
                    },
                    headers=headers
                ) as response:
                    if response.status_code != 200:
                        yield f"Error: HTTP {response.status_code}"
                        return
                        
                    async for line in response.aiter_lines():
                        if line:
                            try:
                                import json
                                data = json.loads(line)
                                if "response" in data:
                                    yield data["response"]
                                if data.get("done", False):
                                    break
                            except json.JSONDecodeError:
                                continue
            except httpx.ConnectError:
                yield "Error: Cannot connect to Ollama server. Please ensure Ollama is running."
            except Exception as e:
                yield f"Error: {str(e)}"
    
    async def chat(self, message: str, model: str = "llama2") -> str:
        """Non-streaming chat with Ollama"""
        headers = {}
        if self.api_key:
            headers["Authorization"] = f"Bearer {self.api_key}"
        
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                f"{self.base_url}/api/generate",
                json={
                    "model": model,
                    "prompt": message,
                    "stream": False
                },
                headers=headers
            )
            
            if response.status_code == 200:
                data = response.json()
                return data.get("response", "")
            else:
                raise Exception(f"Ollama error: HTTP {response.status_code}")
    
    async def list_models(self) -> list:
        """List available models"""
        async with httpx.AsyncClient(timeout=10.0) as client:
            try:
                response = await client.get(f"{self.base_url}/api/tags")
                if response.status_code == 200:
                    data = response.json()
                    return data.get("models", [])
            except Exception:
                pass
        return []
