"""Image quantization for e-ink display."""

from enum import Enum

import hitherdither
from PIL import Image, ImageEnhance

from ..config import DisplayConfig


class DitherMethod(str, Enum):
    """Available dithering methods."""
    FLOYD_STEINBERG = "floyd-steinberg"
    JARVIS = "jarvis-judice-ninke"
    STUCKI = "stucki"
    ATKINSON = "atkinson"
    BURKES = "burkes"
    SIERRA3 = "sierra3"
    SIERRA2 = "sierra2"
    BAYER = "bayer"
    YLILUOMA = "yliluoma"


class ImageQuantizer:
    """Quantizes images to display palette using hitherdither."""
    
    SATURATION_BOOST = 1.4
    DEFAULT_METHOD = DitherMethod.JARVIS
    
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
    
    def quantize(
        self, 
        image: Image.Image, 
        method: DitherMethod = None,
    ) -> Image.Image:
        """Quantize image to display palette with dithering.
        
        Args:
            image: Input image
            method: Dithering method (default: jarvis for smooth gradients)
        """
        method = method or self.DEFAULT_METHOD
        
        if image.mode != "RGB":
            image = image.convert("RGB")
        
        image = image.resize(
            (self._config.width, self._config.height), 
            Image.Resampling.LANCZOS
        )
        
        enhancer = ImageEnhance.Color(image)
        image = enhancer.enhance(self.SATURATION_BOOST)
        if method == DitherMethod.BAYER:
            dithered = hitherdither.ordered.bayer.bayer_dithering(
                image, self._palette, [256//4, 256//4, 256//4], order=8
            )
        elif method == DitherMethod.YLILUOMA:
            dithered = hitherdither.ordered.yliluoma.yliluomas_1_ordered_dithering(
                image, self._palette, order=8
            )
        else:
            dithered = hitherdither.diffusion.error_diffusion_dithering(
                image, self._palette, method=method.value, order=2
            )
        
        return dithered.convert("RGB")
