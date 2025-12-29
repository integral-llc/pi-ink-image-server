"""FastAPI application factory."""

import io
from dataclasses import dataclass, field
from datetime import datetime

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.responses import HTMLResponse, Response

from .adapters.openai_adapter import OpenAIAdapter
from .config import DisplayConfig, FontConfig, QuoteConfig
from .models import TimeOfDay
from .services.art_service import ArtService

load_dotenv()


@dataclass
class GenerationState:
    """Tracks the last generated art."""
    last_image: bytes | None = None
    last_prompt: str | None = None
    last_quote: str | None = None
    last_artist: str | None = None
    last_time_of_day: str | None = None
    last_generated_at: datetime | None = None
    generation_count: int = 0


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

    # State for tracking last generation
    state = GenerationState()
    
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

    @app.get("/status")
    async def status():
        """Detailed status including last generation info."""
        return {
            "status": "ok",
            "timestamp": datetime.now().isoformat(),
            "last_generation": {
                "generated_at": state.last_generated_at.isoformat() if state.last_generated_at else None,
                "prompt": state.last_prompt,
                "quote": state.last_quote,
                "artist": state.last_artist,
                "time_of_day": state.last_time_of_day,
            } if state.last_generated_at else None,
            "generation_count": state.generation_count,
        }

    @app.get("/art/latest")
    async def get_latest_art():
        """Return the last generated art image."""
        if not state.last_image:
            raise HTTPException(status_code=404, detail="No art generated yet")

        return Response(
            content=state.last_image,
            media_type="image/png",
            headers={
                "X-Generated-At": state.last_generated_at.isoformat() if state.last_generated_at else "",
                "X-Time-Of-Day": state.last_time_of_day or "",
                "Cache-Control": "public, max-age=60",
            },
        )
    
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
            image_data = img_bytes.getvalue()

            import re
            def sanitize_header(s: str) -> str:
                return re.sub(r'[^\x20-\x7E]', ' ', s[:200]).strip()

            safe_prompt = sanitize_header(full_prompt)
            safe_quote = sanitize_header(quote)

            # Update state with last generation
            state.last_image = image_data
            state.last_prompt = full_prompt
            state.last_quote = quote
            state.last_artist = artist.name if artist else None
            state.last_time_of_day = time_of_day.value
            state.last_generated_at = datetime.now()
            state.generation_count += 1

            headers = {
                "X-Time-Of-Day": time_of_day.value,
                "X-Prompt": safe_prompt,
                "X-Quote": safe_quote,
            }

            if artist:
                headers["X-Artist"] = sanitize_header(artist.name)
                headers["X-Artist-Style"] = sanitize_header(artist.style)

            return Response(
                content=image_data,
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
    
    @app.get("/tv", response_class=HTMLResponse)
    async def tv_display(
        width: int = 1920,
        height: int = 1080,
        colors: int = 7,
        interval: int = 30,
    ):
        """Self-refreshing TV display page for Chromecast/Fire TV.
        
        Args:
            width: Display width (default: 1920 for 1080p TV)
            height: Display height (default: 1080)
            colors: Number of colors (default: 7 for full color TV)
            interval: Refresh interval in minutes (default: 30)
        """
        interval_ms = interval * 60 * 1000
        return f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Pi2W Art Display</title>
    <style>
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        html, body {{ width: 100%; height: 100%; background: #000; overflow: hidden; }}
        #art {{ 
            width: 100vw; 
            height: 100vh; 
            object-fit: contain;
            opacity: 0;
            transition: opacity 1s ease-in-out;
        }}
        #art.loaded {{ opacity: 1; }}
        #info {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            color: rgba(255,255,255,0.5);
            font-family: system-ui, sans-serif;
            font-size: 14px;
            text-shadow: 1px 1px 2px rgba(0,0,0,0.8);
        }}
    </style>
</head>
<body>
    <img id="art" alt="AI Generated Art">
    <div id="info"></div>
    <script>
        const width = {width};
        const height = {height};
        const colors = {colors};
        const intervalMs = {interval_ms};
        
        async function loadArt() {{
            const img = document.getElementById('art');
            const info = document.getElementById('info');
            img.classList.remove('loaded');
            
            const basePath = window.location.pathname.replace(/\/tv$/, '');
            const url = `${{basePath}}/art?width=${{width}}&height=${{height}}&colors=${{colors}}&t=${{Date.now()}}`;
            
            try {{
                const response = await fetch(url);
                if (!response.ok) throw new Error('Failed to load');
                
                const blob = await response.blob();
                const objectUrl = URL.createObjectURL(blob);
                
                const artist = response.headers.get('X-Artist') || '';
                const timeOfDay = response.headers.get('X-Time-Of-Day') || '';
                
                img.onload = () => {{
                    img.classList.add('loaded');
                    URL.revokeObjectURL(img.src);
                }};
                img.src = objectUrl;
                
                const now = new Date();
                const next = new Date(now.getTime() + intervalMs);
                info.textContent = artist ? `${{artist}} · Next: ${{next.toLocaleTimeString()}}` : '';
            }} catch (e) {{
                info.textContent = 'Loading failed, retrying...';
                setTimeout(loadArt, 10000);
            }}
        }}
        
        loadArt();
        setInterval(loadArt, intervalMs);
    </script>
</body>
</html>"""
    
    return app
