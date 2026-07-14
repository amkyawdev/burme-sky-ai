import os
import httpx
from typing import Optional, Dict, Any


class WebhookHandler:
    def __init__(self):
        self.webhook_url = os.getenv("WEBHOOK_URL", "")
    
    async def send_notification(
        self, 
        message: str, 
        event_type: str = "chat_message",
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Send a notification to the configured webhook URL"""
        if not self.webhook_url:
            return False
        
        payload = {
            "event": event_type,
            "message": message,
            "timestamp": self._get_timestamp(),
        }
        
        if metadata:
            payload["metadata"] = metadata
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                response = await client.post(
                    self.webhook_url,
                    json=payload,
                    headers={
                        "Content-Type": "application/json",
                        "User-Agent": "BurmeSkyAI/1.0"
                    }
                )
                return response.status_code in (200, 201, 202, 204)
        except Exception as e:
            print(f"Webhook error: {e}")
            return False
    
    async def send_chat_started(self, message: str) -> bool:
        """Notify when a new chat session starts"""
        return await self.send_notification(
            message=f"New chat started: {message[:100]}",
            event_type="chat_started"
        )
    
    async def send_chat_completed(self, message: str, response: str) -> bool:
        """Notify when a chat completes"""
        return await self.send_notification(
            message=f"Chat completed",
            event_type="chat_completed",
            metadata={
                "message": message,
                "response_length": len(response)
            }
        )
    
    def _get_timestamp(self) -> str:
        """Get current ISO timestamp"""
        from datetime import datetime
        return datetime.now().isoformat()
