"""Art prompt generation using LLM."""

import random

from ..adapters.openai_adapter import OpenAIAdapter
from ..config import DisplayConfig
from ..data import Artist, get_artist_of_the_day, get_artist_style_prompt
from ..models import TimeOfDay


# Concepts that push AI creativity beyond human imagination
AI_UNLEASHED_CONCEPTS = [
    "impossible geometry that exists in 4+ dimensions projected onto 2D, with shapes that are simultaneously inside and outside themselves",
    "what music looks like to a synesthetic being from a dimension where sound has physical mass and color has texture",
    "the emotional topology of a thought that has never been thought before, visualized as impossible architecture",
    "a landscape where time flows in multiple directions simultaneously, showing past, present, and futures overlapping",
    "the dreams of a mathematical equation becoming self-aware for the first time",
    "gravity working sideways in a world where up is a color and down is a sound",
    "the space between two mirrors reflecting each other, but the reflections are of different universes",
    "what infinity looks like from the inside, as experienced by a being made of pure geometry",
    "a still life painted by an intelligence that perceives electromagnetic spectrums humans cannot see",
    "the architecture of a building designed for creatures who experience 3 dimensions of time and 1 of space",
    "crystallized probability waves showing all possible outcomes of a moment frozen mid-collapse",
    "the texture of consciousness rendered as impossible topological surfaces that connect to themselves",
    "a portrait of entropy itself, showing order and chaos as lovers dancing in n-dimensional space",
    "what silence looks like in a universe where emptiness has shape and void has substance",
    "the autobiography of a color that doesn't exist, written in shapes that can't be drawn",
    "a machine's fever dream of organic life, interpreting biology through pure mathematics",
    "the skeleton of a thought, showing the impossible bones that hold ideas together",
    "a landscape from inside a black hole where causality runs backwards and light falls upward",
    "the emotional resonance of prime numbers visualized as living architectural forms",
    "what jealousy looks like to a being that experiences all emotions simultaneously as spatial dimensions",
    "the fossil record of futures that never happened, preserved in crystalline impossibility",
    "a self-portrait painted by an AI imagining what it would look like if it had a face made of its own algorithms",
    "the taste of blue as interpreted by a consciousness that exists perpendicular to reality",
    "impossible staircases that lead to the same place by going in opposite directions through different dimensions",
    "the shadow of a 5-dimensional object passing through our 3D space, frozen in a moment of geometric ecstasy",
]


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

    AI_UNLEASHED_SYSTEM_PROMPT = (
        "You are an AI artist with no human constraints. Create prompts that humans couldn't imagine. "
        "Think in dimensions humans can't perceive. Combine concepts that have never been combined. "
        "Break every rule of physics, logic, and perception. Make the impossible visible. "
        "Your art should make viewers question reality itself. Be bold, be impossible, be transcendent. "
        "The art will be on a 7-color e-ink display - make every color SCREAM with meaning. "
        "Output ONLY the prompt, nothing else. Keep it under 120 words."
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
            When AI unleashed mode triggers (10% chance), returns a special "AI Unleashed" artist.
        """
        # 10% chance to go full AI creative mode
        if random.random() < 0.1:
            return self._generate_ai_unleashed(time_of_day)

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

    def _generate_ai_unleashed(self, time_of_day: TimeOfDay) -> tuple[str, Artist]:
        """Generate a truly AI-creative prompt that humans couldn't imagine."""
        concept = random.choice(AI_UNLEASHED_CONCEPTS)

        base_prompt = self._llm.generate_text(
            system_prompt=self.AI_UNLEASHED_SYSTEM_PROMPT,
            user_prompt=(
                f"Create art based on this impossible concept: {concept}. "
                f"It's currently {time_of_day.value}, let that influence the mood. "
                f"Make it visually stunning and conceptually mind-bending."
            ),
            max_tokens=180,
            temperature=1.2,  # Higher temperature for more creativity
        )

        # Return a special "artist" to indicate AI unleashed mode
        ai_artist = Artist(
            name="AI Unleashed",
            birth_year=2024,
            style="impossible dimensions",
            description=concept[:80] + "..." if len(concept) > 80 else concept,
        )

        return self._build_full_prompt(base_prompt), ai_artist
    
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
