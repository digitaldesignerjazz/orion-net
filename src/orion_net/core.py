"""
Core abstractions for Orion Net.

Long-range networking with constellation formation and hooks for Lyra emotional modulation.
"""

from __future__ import annotations

import time
import random
from dataclasses import dataclass, field
from enum import Enum, auto
from typing import Dict, List, Optional, Tuple


class LinkQuality(Enum):
    STABLE = auto()
    VOLATILE = auto()
    EMERGING = auto()
    DEGRADED = auto()


@dataclass
class OrionLink:
    """A long-range Orion (constellation-scale) link, typically over hyperspace."""
    peer_id: str
    address: str
    quality: LinkQuality = LinkQuality.EMERGING
    latency_ms: float = 0.0
    stability: float = 0.5
    emotional_resonance: float = 0.5  # from Lyra
    trust: float = 0.5
    last_updated: float = field(default_factory=time.time)

    def score(self, lyra_bias: float = 0.5) -> float:
        tech = (self.stability * 0.6 + (1.0 / max(1.0, self.latency_ms / 100)) * 0.4)
        emotional = self.emotional_resonance * lyra_bias + self.trust * (1 - lyra_bias) * 0.5
        return (tech * (1 - lyra_bias) + emotional * lyra_bias)


@dataclass
class OrionConstellation:
    """A named group of nodes/agents forming a resilient long-range constellation."""
    name: str
    purpose: str
    members: List[str] = field(default_factory=list)
    created_at: float = field(default_factory=time.time)
    resonance_threshold: float = 0.6

    def add_member(self, peer_id: str):
        if peer_id not in self.members:
            self.members.append(peer_id)

    def is_viable(self, scores: Dict[str, float]) -> bool:
        if not self.members:
            return False
        avg = sum(scores.get(m, 0.0) for m in self.members) / len(self.members)
        return avg >= self.resonance_threshold


class ResonantOrionRouter:
    """
    Orion Net router with Lyra emotional modulation hooks.
    """

    def __init__(self, lyra_params: Optional[Dict[str, float]] = None):
        self.lyra_params = lyra_params or {
            "devotion": 0.7,
            "curiosity": 0.6,
            "caution": 0.4,
            "play": 0.5,
        }
        self.links: Dict[str, OrionLink] = {}
        self.constellations: Dict[str, OrionConstellation] = {}

    def register_link(self, link: OrionLink):
        self.links[link.peer_id] = link

    def update_link_from_lyra(self, peer_id: str, emotional_resonance: float, trust: float):
        if peer_id in self.links:
            link = self.links[peer_id]
            link.emotional_resonance = emotional_resonance
            link.trust = trust
            link.last_updated = time.time()

    def score_link(self, peer_id: str) -> float:
        link = self.links.get(peer_id)
        if not link:
            return 0.2
        lyra_bias = self.lyra_params.get("devotion", 0.5) * 0.5 + self.lyra_params.get("curiosity", 0.5) * 0.5
        return link.score(lyra_bias=lyra_bias)

    def choose_best_link(self, candidates: List[str]) -> Optional[str]:
        scored = []
        for pid in candidates:
            if pid in self.links:
                s = self.score_link(pid)
                # Play adds some exploration noise
                noise = random.uniform(-self.lyra_params.get("play", 0.5) * 0.1, self.lyra_params.get("play", 0.5) * 0.1)
                scored.append((s + noise, pid))
        if not scored:
            return None
        scored.sort(reverse=True)
        return scored[0][1]

    def form_constellation(self, name: str, purpose: str, min_members: int = 3) -> Optional[OrionConstellation]:
        viable = [
            pid for pid in self.links
            if self.score_link(pid) > 0.5
        ]
        if len(viable) < min_members:
            return None
        const = OrionConstellation(name=name, purpose=purpose)
        scored = sorted([(self.score_link(pid), pid) for pid in viable], reverse=True)
        for _, pid in scored[:min_members + 1]:
            const.add_member(pid)
        self.constellations[name] = const
        return const

    def get_status(self) -> Dict:
        return {
            "links": len(self.links),
            "constellations": len(self.constellations),
            "lyra_params": self.lyra_params,
        }
