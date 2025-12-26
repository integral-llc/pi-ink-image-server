"""Art prompt generation using LLM."""

from ..adapters.openai_adapter import OpenAIAdapter
from ..config import DisplayConfig
from ..data import Artist, get_artist_of_the_day, get_artist_style_prompt
from ..models import TimeOfDay


class ArtPromptGenerator:
    """Generates art prompts using LLM."""
    
    SYSTEM_PROMPT = (
        "You are an expert art director creating prompts for DALL-E 3. "
        "Generate vivid, striking, visually rich image prompts. "
        "Focus on: bold colors, dramatic lighting, strong composition, emotional impact. "
        "Avoid: dull, muted, flat, generic descriptions. "
        "The art will be displayed on a 7-color e-ink display (black, white, red, yellow, green, blue, orange). "
        "Make colors POP. Use high contrast. Think gallery-worthy, eye-catching art. "
        "Output ONLY the prompt, nothing else. Keep it under 100 words."
    )
    
    def __init__(self, llm: OpenAIAdapter, display_config: DisplayConfig):
        self._llm = llm
        self._display_config = display_config
    
    def generate(
        self, 
        time_of_day: TimeOfDay, 
        style: str | None = None,
        use_artist_of_day: bool = True,
    ) -> tuple[str, Artist | None]:
        """Generate art prompt for given time of day.
        
        Returns:
            Tuple of (prompt, artist) where artist is None if not using artist of day.
        """
        artist = None
        if use_artist_of_day and style is None:
            artist = get_artist_of_the_day()
            if artist:
                style = get_artist_style_prompt(artist)
        
        style_hint = f" {style}" if style else ""
        
        base_prompt = self._llm.generate_text(
            system_prompt=self.SYSTEM_PROMPT,
            user_prompt=f"Create a stunning {time_of_day.value} scene{style_hint}. Make it vibrant and visually striking.",
            max_tokens=150,
            temperature=1.0,
        )
        
        return self._build_full_prompt(base_prompt), artist
    
    def _build_full_prompt(self, base: str) -> str:
        """Build complete prompt with display requirements."""
        colors = ", ".join(self._display_config.colors)
        return (
            f"{base} "
            f"Vibrant saturated colors from this palette: {colors}. "
            f"High contrast, bold graphic shapes, dramatic lighting. "
            f"No muddy colors, no grey, no brown. Crisp and vivid. "
            f"Full bleed artwork with no borders, no frames, no color bars, no test patterns, no decorative edges. "
            f"The scene should extend to all edges of the image."
        )
    
    def build_custom_prompt(self, prompt: str) -> str:
        """Build prompt from custom user input."""
        colors = ", ".join(self._display_config.colors)
        return (
            f"{prompt}. "
            f"Art suitable for e-ink display with limited colors: {colors}. "
            f"High contrast, bold shapes, minimal gradients."
        )
