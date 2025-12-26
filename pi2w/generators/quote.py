"""Quote generation using LLM."""

import random

from ..adapters.openai_adapter import OpenAIAdapter
from ..config import QuoteConfig


class QuoteGenerator:
    """Generates inspirational quotes using LLM."""
    
    SYSTEM_PROMPT = (
        "You generate short, powerful, ORIGINAL quotes. "
        "Be creative and unexpected. Avoid clichés and common phrases. "
        "Use vivid imagery or unexpected metaphors. "
        "Keep it under 12 words. No attribution - just the quote. "
        "Never repeat quotes you've generated before. Be fresh and surprising."
    )
    
    def __init__(self, llm: OpenAIAdapter, config: QuoteConfig):
        self._llm = llm
        self._config = config
    
    def generate(self) -> str:
        """Generate a random inspirational quote."""
        theme = random.choice(self._config.themes)
        result = self._llm.generate_text(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=f"Generate an original quote about {theme}.",
            max_tokens=50,
            temperature=self._config.temperature,
        )
        return result.strip('"')
