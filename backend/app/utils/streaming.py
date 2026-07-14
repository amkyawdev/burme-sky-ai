import asyncio
import json
from typing import AsyncGenerator, Dict, Any


class StreamBuffer:
    """Buffer for managing streaming responses"""
    
    def __init__(self):
        self.buffer = ""
        self.last_word_end = 0
    
    def add(self, chunk: str) -> str:
        """Add a chunk and return complete words"""
        self.buffer += chunk
        
        # Find the last space or newline
        words = self.buffer.split()
        if len(words) > 5:  # Return at least 5 words
            self.buffer = words[-1]
            return ' '.join(words[:-1])
        
        return ""
    
    def flush(self) -> str:
        """Flush remaining buffer"""
        result = self.buffer
        self.buffer = ""
        return result


async def stream_response(
    generator: AsyncGenerator[str, None],
    chunk_size: int = 20
) -> AsyncGenerator[str, None]:
    """Stream a response with chunking"""
    buffer = StreamBuffer()
    
    async for chunk in generator:
        output = buffer.add(chunk)
        if output:
            yield output
    
    # Flush remaining
    remaining = buffer.flush()
    if remaining:
        yield remaining


def create_sse_message(event: str, data: Dict[str, Any]) -> str:
    """Create a Server-Sent Events message"""
    return f"event: {event}\ndata: {json.dumps(data)}\n\n"


def create_sse_data(data: Dict[str, Any]) -> str:
    """Create a simple SSE data message"""
    return f"data: {json.dumps(data)}\n\n"
