"""OpenAI API adapter."""

import os
from typing import Protocol

from openai import OpenAI


class LLMClient(Protocol):
    """Protocol for LLM operations."""
    def generate_text(self, system_prompt: str, user_prompt: str, 
                      max_tokens: int, temperature: float) -> str: ...
    
    def generate_image(self, prompt: str, size: str) -> str: ...


class OpenAIAdapter:
    """Adapts OpenAI client to our LLMClient protocol."""
    
    def __init__(self, api_key: str | None = None):
        self._client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
    
    def generate_text(self, system_prompt: str, user_prompt: str,
                      max_tokens: int = 50, temperature: float = 0.9) -> str:
        """Generate text using chat completion."""
        response = self._client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt},
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )
        return response.choices[0].message.content.strip()
    
    def generate_image(self, prompt: str, size: str = "1792x1024") -> str:
        """Generate image and return URL."""
        response = self._client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            size=size,
            quality="standard",
            n=1,
        )
        return response.data[0].url
