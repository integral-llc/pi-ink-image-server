"""Image analysis utilities."""

from PIL import Image

from ..models import TextColors, TextPosition


class ImageAnalyzer:
    """Analyzes image properties."""
    
    @staticmethod
    def get_region_brightness(image: Image.Image, position: TextPosition) -> float:
        """Analyze average brightness of a region. Returns 0-255."""
        region = image.crop((
            position.x, 
            position.y, 
            position.x + position.width, 
            position.y + position.height
        ))
        grayscale = region.convert("L")
        pixels = list(grayscale.getdata())
        return sum(pixels) / len(pixels) if pixels else 128
    
    @staticmethod
    def get_optimal_text_colors(brightness: float, threshold: float = 140) -> TextColors:
        """Determine best text colors based on background brightness."""
        if brightness > threshold:
            return TextColors(text=(0, 0, 0), shadow=(255, 255, 255))
        return TextColors(text=(255, 255, 255), shadow=(0, 0, 0))
