"""Image quantization for e-ink display."""

import hitherdither
from PIL import Image, ImageEnhance

from ..config import DisplayConfig


class ImageQuantizer:
    """Quantizes images to display palette using hitherdither."""
    
    SATURATION_BOOST = 1.4
    
    def __init__(self, config: DisplayConfig):
        self._config = config
        self._palette = self._create_palette()
    
    def _create_palette(self) -> hitherdither.palette.Palette:
        """Create hitherdither palette from config."""
        hex_colors = [
            (r << 16) | (g << 8) | b 
            for r, g, b in self._config.palette_rgb
        ]
        return hitherdither.palette.Palette(hex_colors)
    
    def quantize(self, image: Image.Image) -> Image.Image:
        """Quantize image to display palette with Floyd-Steinberg dithering."""
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        image = image.resize(
            (self._config.width, self._config.height), 
            Image.Resampling.LANCZOS
        )
        
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(self.SATURATION_BOOST)
        
        dithered = hitherdither.diffusion.error_diffusion_dithering(
            image, self._palette, method="floyd-steinberg", order=2
        )
        
        return dithered.convert("RGB")
