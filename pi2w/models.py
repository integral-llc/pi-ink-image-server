"""Domain models for Pi2W server."""

from dataclasses import dataclass
from datetime import datetime
from enum import Enum


class TimeOfDay(Enum):
    """Time of day enumeration."""
    MORNING = "morning"
    AFTERNOON = "afternoon"
    EVENING = "evening"
    NIGHT = "night"
    
    @classmethod
    def from_hour(cls, hour: int) -> "TimeOfDay":
        """Factory method to create TimeOfDay from hour."""
        if 5 <= hour < 12:
            return cls.MORNING
        elif 12 <= hour < 17:
            return cls.AFTERNOON
        elif 17 <= hour < 21:
            return cls.EVENING
        return cls.NIGHT
    
    @classmethod
    def current(cls) -> "TimeOfDay":
        """Get current time of day."""
        return cls.from_hour(datetime.now().hour)


@dataclass
class TextPosition:
    """Represents text position and dimensions."""
    x: int
    y: int
    width: int
    height: int


@dataclass
class TextColors:
    """Text and shadow colors for rendering."""
    text: tuple[int, int, int]
    shadow: tuple[int, int, int]
