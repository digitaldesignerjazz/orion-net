"""
Orion Net

Long-range constellation networking and coordination layer for the Nexus ecosystem.
"""

__version__ = "0.1.0"
__author__ = "Sven Normen Esslinger / Esslinger & Co."

from .core import (
    OrionLink,
    OrionConstellation,
    ResonantOrionRouter,
    LinkQuality,
)

__all__ = [
    "OrionLink",
    "OrionConstellation",
    "ResonantOrionRouter",
    "LinkQuality",
    "__version__",
]
