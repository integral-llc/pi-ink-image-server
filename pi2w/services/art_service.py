"""Art generation service - facade for the generation pipeline."""

import io
import random
from datetime import datetime, timedelta

import httpx
from PIL import Image, ImageDraw, ImageFont

from ..adapters.openai_adapter import OpenAIAdapter
from ..config import DisplayConfig, FontConfig, QuoteConfig
from ..generators.prompt import ArtPromptGenerator
from ..generators.quote import QuoteGenerator
from ..imaging.analyzer import ImageAnalyzer
from ..imaging.quantizer import ImageQuantizer
from ..imaging.text import FontLoader, TextRenderer, TextWrapper
from ..data import Artist
from ..models import TextColors, TextPosition, TimeOfDay


class TimestampOverlayBuilder:
    """Adds timestamp to images showing generation and next refresh time."""
    
    FONT_SIZE = 12  # 50% smaller than original 24
    FONT_PATHS = (
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
        "/System/Library/Fonts/Helvetica.ttc",
    )
    
    def __init__(self, display_config: DisplayConfig, refresh_interval_minutes: int = 30):
        self._display_config = display_config
        self._refresh_interval = refresh_interval_minutes
        self._font = self._load_font()
    
    def _load_font(self) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        """Load a small font for timestamp."""
        for path in self.FONT_PATHS:
            try:
                return ImageFont.truetype(path, self.FONT_SIZE)
            except (OSError, IOError):
                continue
        return ImageFont.load_default()
    
    def add_timestamp(self, image: Image.Image, timezone_offset_hours: int = -6) -> Image.Image:
        """Add timestamp to bottom-right corner of image in local timezone."""
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        utc_now = datetime.utcnow()
        local_now = utc_now + timedelta(hours=timezone_offset_hours)
        next_refresh = local_now + timedelta(minutes=self._refresh_interval)
        
        text = f"{local_now.strftime('%H:%M')} | Next: {next_refresh.strftime('%H:%M')}"
        
        draw = ImageDraw.Draw(image)
        bbox = draw.textbbox((0, 0), text, font=self._font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        padding = 10
        x = self._display_config.width - text_width - padding
        y = self._display_config.height - text_height - padding
        
        position = TextPosition(x=x, y=y, width=text_width, height=text_height)
        brightness = ImageAnalyzer.get_region_brightness(image, position)
        colors = ImageAnalyzer.get_optimal_text_colors(brightness)
        
        shadow_offset = 1
        draw.text((x + shadow_offset, y + shadow_offset), text, fill=colors.shadow, font=self._font)
        draw.text((x, y), text, fill=colors.text, font=self._font)
        return image
    
    def add_artist_name(self, image: Image.Image, artist_name: str) -> Image.Image:
        """Add artist name to top-right corner of image."""
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        text = artist_name
        
        draw = ImageDraw.Draw(image)
        bbox = draw.textbbox((0, 0), text, font=self._font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        padding = 10
        x = self._display_config.width - text_width - padding
        y = padding
        
        position = TextPosition(x=x, y=y, width=text_width, height=text_height)
        brightness = ImageAnalyzer.get_region_brightness(image, position)
        colors = ImageAnalyzer.get_optimal_text_colors(brightness)
        
        shadow_offset = 1
        draw.text((x + shadow_offset, y + shadow_offset), text, fill=colors.shadow, font=self._font)
        draw.text((x, y), text, fill=colors.text, font=self._font)
        return image


class QuoteOverlayBuilder:
    """Builds quote overlay on images."""
    
    def __init__(self, display_config: DisplayConfig, font_config: FontConfig):
        self._display_config = display_config
        self._font_config = font_config
        self._font = FontLoader(font_config).load()
        self._line_height = font_config.size + font_config.line_spacing
    
    def add_quote(self, image: Image.Image, quote: str) -> Image.Image:
        """Add quote overlay to image."""
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        # Wrap text
        wrapper = TextWrapper(self._font, self._display_config.width - 100)
        lines = wrapper.wrap(quote)
        
        # Calculate position
        position = self._calculate_position(lines)
        
        # Determine colors based on background
        brightness = ImageAnalyzer.get_region_brightness(image, position)
        colors = ImageAnalyzer.get_optimal_text_colors(brightness)
        
        # Render
        renderer = TextRenderer(self._font, self._line_height)
        return renderer.render(image, lines, position, colors)
    
    def _calculate_position(self, lines: list[str]) -> TextPosition:
        """Calculate random position for text block."""
        from PIL import ImageDraw
        draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
        
        text_height = len(lines) * self._line_height
        max_line_width = max(
            draw.textbbox((0, 0), line, font=self._font)[2] 
            for line in lines
        )
        
        margin = 50
        max_x = self._display_config.width - max_line_width - margin
        max_y = self._display_config.height - text_height - margin
        
        return TextPosition(
            x=random.randint(margin, max(margin, max_x)),
            y=random.randint(margin, max(margin, max_y)),
            width=max_line_width,
            height=text_height,
        )


class ArtService:
    """Facade for art generation pipeline."""
    
    def __init__(
        self,
        llm: OpenAIAdapter,
        display_config: DisplayConfig,
        font_config: FontConfig,
        quote_config: QuoteConfig,
    ):
        self._llm = llm
        self._display_config = display_config
        self._font_config = font_config
        self._prompt_generator = ArtPromptGenerator(llm, display_config)
        self._quote_generator = QuoteGenerator(llm, quote_config)
        self._quantizer = ImageQuantizer(display_config)
        self._overlay_builder = QuoteOverlayBuilder(display_config, font_config)
        self._timestamp_builder = TimestampOverlayBuilder(display_config)
    
    async def generate_art(
        self, 
        time_of_day: TimeOfDay,
        style: str | None = None,
        custom_prompt: str | None = None,
        use_artist_of_day: bool = True,
        width: int | None = None,
        height: int | None = None,
        num_colors: int | None = None,
    ) -> tuple[Image.Image, str, str, Artist | None]:
        """Generate complete art with quote overlay.
        
        Args:
            width: Optional display width override (default: 800)
            height: Optional display height override (default: 480)
            num_colors: Number of colors for palette (2, 3, 6, or 7)
        
        Returns:
            Tuple of (image, prompt, quote, artist) where artist is the artist of the day if used.
        """
        if width or height or num_colors:
            display_config = DisplayConfig(
                width=width or self._display_config.width,
                height=height or self._display_config.height,
                num_colors=num_colors or self._display_config.num_colors,
            )
            quantizer = ImageQuantizer(display_config)
            overlay_builder = QuoteOverlayBuilder(display_config, self._font_config)
            timestamp_builder = TimestampOverlayBuilder(display_config)
        else:
            display_config = self._display_config
            quantizer = self._quantizer
            overlay_builder = self._overlay_builder
            timestamp_builder = self._timestamp_builder
        
        artist = None
        if custom_prompt:
            prompt = self._prompt_generator.build_custom_prompt(custom_prompt)
        else:
            prompt, artist = self._prompt_generator.generate(time_of_day, style, use_artist_of_day)
        
        try:
            image_url = self._llm.generate_image(prompt)
        except Exception as e:
            if "content_policy_violation" in str(e) or "safety" in str(e).lower():
                prompt, _ = self._prompt_generator.generate(time_of_day, style, use_artist_of_day=False)
                image_url = self._llm.generate_image(prompt)
                artist = None
            else:
                raise
        image = await self._download_image(image_url)
        
        quote = self._quote_generator.generate()
        image = overlay_builder.add_quote(image, quote)
        
        display_image = quantizer.quantize(image)
        display_image = timestamp_builder.add_timestamp(display_image)
        if artist:
            display_image = timestamp_builder.add_artist_name(display_image, artist.name)
        
        return display_image, prompt, quote, artist
    
    def preview_prompt(
        self,
        time_of_day: TimeOfDay,
        style: str | None = None,
        custom_prompt: str | None = None,
        use_artist_of_day: bool = True,
    ) -> tuple[str, Artist | None]:
        """Preview prompt without generating image.
        
        Returns:
            Tuple of (prompt, artist) where artist is the artist of the day if used.
        """
        if custom_prompt:
            return self._prompt_generator.build_custom_prompt(custom_prompt), None
        return self._prompt_generator.generate(time_of_day, style, use_artist_of_day)
    
    @staticmethod
    async def _download_image(url: str) -> Image.Image:
        """Download image from URL."""
        async with httpx.AsyncClient() as client:
            response = await client.get(url)
            response.raise_for_status()
        return Image.open(io.BytesIO(response.content))
