"""FastAPI application factory."""

import io
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import Response

from .adapters.openai_adapter import OpenAIAdapter
from .config import DisplayConfig, FontConfig, QuoteConfig
from .models import TimeOfDay
from .services.art_service import ArtService

load_dotenv()


def create_app() -> FastAPI:
    """Create and configure FastAPI application."""
    
    # Configuration
    display_config = DisplayConfig()
    font_config = FontConfig()
    quote_config = QuoteConfig()
    
    # Dependencies
    llm = OpenAIAdapter()
    art_service = ArtService(llm, display_config, font_config, quote_config)
    
    # Application
    app = FastAPI(title="Pi2W Content Server", version="0.2.0")
    
    @app.get("/")
    async def root():
        """Server info."""
        return {
            "name": "Pi2W Content Server",
            "version": "0.2.0",
            "display": {
                "width": display_config.width,
                "height": display_config.height,
                "colors": display_config.colors,
            },
            "features": ["ai_art", "dashboard", "focus_mode", "messages", "recipes"],
        }
    
    @app.get("/health")
    async def health():
        """Health check endpoint."""
        return {"status": "ok", "timestamp": datetime.now().isoformat()}
    
    # Valid display parameter ranges
    MIN_SIZE = 100
    MAX_SIZE = 4096
    VALID_COLORS = {2, 3, 6, 7}
    
    @app.get("/art")
    async def get_art(
        style: str | None = None, 
        prompt: str | None = None,
        width: int | None = None,
        height: int | None = None,
        colors: int | None = None,
    ):
        """Generate AI art based on time of day.
        
        Args:
            style: Optional art style
            prompt: Optional custom prompt
            width: Display width (default: 800, range: 100-4096)
            height: Display height (default: 480, range: 100-4096)
            colors: Number of colors (2, 3, 6, or 7). Default: 6 for Spectra 6
        """
        # Validate size parameters
        if width is not None and not (MIN_SIZE <= width <= MAX_SIZE):
            raise HTTPException(
                status_code=400, 
                detail=f"width must be between {MIN_SIZE} and {MAX_SIZE}"
            )
        if height is not None and not (MIN_SIZE <= height <= MAX_SIZE):
            raise HTTPException(
                status_code=400, 
                detail=f"height must be between {MIN_SIZE} and {MAX_SIZE}"
            )
        if colors is not None and colors not in VALID_COLORS:
            raise HTTPException(
                status_code=400,
                detail=f"colors must be one of {sorted(VALID_COLORS)}"
            )
        
        time_of_day = TimeOfDay.current()
        
        try:
            image, full_prompt, quote, artist = await art_service.generate_art(
                time_of_day, style, prompt, width=width, height=height, num_colors=colors
            )
            
            img_bytes = io.BytesIO()
            image.save(img_bytes, format="PNG")
            img_bytes.seek(0)
            
            import re
            def sanitize_header(s: str) -> str:
                return re.sub(r'[^\x20-\x7E]', ' ', s[:200]).strip()
            
            safe_prompt = sanitize_header(full_prompt)
            safe_quote = sanitize_header(quote)
            
            headers = {
                "X-Time-Of-Day": time_of_day.value,
                "X-Prompt": safe_prompt,
                "X-Quote": safe_quote,
            }
            
            if artist:
                headers["X-Artist"] = sanitize_header(artist.name)
                headers["X-Artist-Style"] = sanitize_header(artist.style)
            
            return Response(
                content=img_bytes.getvalue(),
                media_type="image/png",
                headers=headers,
            )
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
    
    @app.get("/art/preview")
    async def preview_art(style: str | None = None, prompt: str | None = None):
        """Preview prompt without generating image."""
        time_of_day = TimeOfDay.current()
        full_prompt, artist = art_service.preview_prompt(time_of_day, style, prompt)
        response = {"time_of_day": time_of_day.value, "prompt": full_prompt}
        if artist:
            response["artist"] = {
                "name": artist.name,
                "birth_year": artist.birth_year,
                "style": artist.style,
                "description": artist.description,
            }
        return response
    
    return app
