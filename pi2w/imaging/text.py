"""Text rendering utilities."""

from PIL import Image, ImageDraw, ImageFont

from ..config import FontConfig
from ..models import TextColors, TextPosition


class FontLoader:
    """Loads fonts with fallback support."""
    
    def __init__(self, config: FontConfig):
        self._config = config
    
    def load(self) -> ImageFont.FreeTypeFont | ImageFont.ImageFont:
        """Load font with fallback chain."""
        for font_path in self._config.paths:
            try:
                return ImageFont.truetype(font_path, self._config.size)
            except (OSError, IOError):
                continue
        return ImageFont.load_default()


class TextWrapper:
    """Wraps text to fit within width constraints."""
    
    def __init__(self, font: ImageFont.FreeTypeFont | ImageFont.ImageFont, max_width: int):
        self._font = font
        self._max_width = max_width
        self._draw = ImageDraw.Draw(Image.new("RGB", (1, 1)))
    
    def wrap(self, text: str) -> list[str]:
        """Wrap text into lines that fit within max_width."""
        words = text.split()
        lines = []
        current_line: list[str] = []
        
        for word in words:
            test_line = " ".join(current_line + [word])
            bbox = self._draw.textbbox((0, 0), test_line, font=self._font)
            if bbox[2] - bbox[0] <= self._max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(" ".join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(" ".join(current_line))
        
        return lines


class TextRenderer:
    """Renders text onto images with shadow effect."""
    
    SHADOW_OFFSETS = (
        (-4, -4), (-4, 4), (4, -4), (4, 4),
        (-4, 0), (4, 0), (0, -4), (0, 4),
        (-2, -2), (-2, 2), (2, -2), (2, 2),
    )
    
    def __init__(self, font: ImageFont.FreeTypeFont | ImageFont.ImageFont, 
                 line_height: int):
        self._font = font
        self._line_height = line_height
    
    def render(self, image: Image.Image, lines: list[str], 
               position: TextPosition, colors: TextColors) -> Image.Image:
        """Render text lines onto image."""
        draw = ImageDraw.Draw(image)
        y_pos = position.y
        
        for line in lines:
            bbox = draw.textbbox((0, 0), line, font=self._font)
            text_width = bbox[2] - bbox[0]
            x = position.x + (position.width - text_width) // 2
            
            # Draw shadow
            for ox, oy in self.SHADOW_OFFSETS:
                draw.text((x + ox, y_pos + oy), line, fill=colors.shadow, font=self._font)
            
            # Draw text
            draw.text((x, y_pos), line, fill=colors.text, font=self._font)
            y_pos += self._line_height
        
        return image
