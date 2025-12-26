"""Configuration dataclasses for Pi2W server."""

from dataclasses import dataclass


PALETTES = {
    2: [  # Black & White
        (0, 0, 0),        # Black
        (255, 255, 255),  # White
    ],
    3: [  # 3-color (black, white, red/yellow)
        (0, 0, 0),        # Black
        (255, 255, 255),  # White
        (255, 0, 0),      # Red
    ],
    6: [  # Spectra 6 (2025 edition) - NO ORANGE
        (0, 0, 0),        # Black
        (255, 255, 255),  # White
        (255, 0, 0),      # Red
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
    ],
    7: [  # 7-color ACeP (older displays)
        (0, 0, 0),        # Black
        (255, 255, 255),  # White
        (255, 0, 0),      # Red
        (255, 255, 0),    # Yellow
        (0, 255, 0),      # Green
        (0, 0, 255),      # Blue
        (255, 128, 0),    # Orange
    ],
}


def get_palette(num_colors: int) -> list[tuple[int, int, int]]:
    """Get palette for given number of colors."""
    return PALETTES.get(num_colors, PALETTES[7])


@dataclass(frozen=True)
class DisplayConfig:
    """Display hardware configuration."""
    width: int = 800
    height: int = 480
    num_colors: int = 6
    
    @property
    def palette_rgb(self) -> list[tuple[int, int, int]]:
        """RGB values for display palette."""
        return get_palette(self.num_colors)
    
    @property
    def colors(self) -> tuple[str, ...]:
        """Color names for display."""
        names = ["black", "white", "red", "yellow", "green", "blue", "orange"]
        return tuple(names[:self.num_colors])


@dataclass(frozen=True)
class FontConfig:
    """Font configuration for text rendering."""
    size: int = 99
    line_spacing: int = 20
    paths: tuple[str, ...] = (
        "/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyreschola-bold.otf",
        "/usr/share/texmf/fonts/opentype/public/tex-gyre/texgyrebonum-bold.otf",
        "/System/Library/Fonts/Supplemental/Trattatello.ttf",
        "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Bold.ttf",
        "/System/Library/Fonts/Times.ttc",
    )


@dataclass(frozen=True)
class QuoteConfig:
    """Quote generation configuration."""
    max_words: int = 12
    temperature: float = 1.2
    themes: tuple[str, ...] = (
        "inner strength and resilience",
        "embracing solitude and self-reliance",
        "facing fear with courage",
        "the power of patience and persistence",
        "finding peace in chaos",
        "the beauty of impermanence",
        "mastering your own mind",
        "rising after failure",
        "the wisdom of silence",
        "strength through adversity",
        "letting go of what doesn't serve you",
        "the courage to be yourself",
    )
