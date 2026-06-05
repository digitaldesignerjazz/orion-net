"""
Orion Net basic demo.

Shows link registration, Lyra-modulated scoring, and constellation formation.

Run: python -m examples.orion_demo
"""

import asyncio
from orion_net import OrionLink, ResonantOrionRouter, LinkQuality


async def main():
    print("=== Orion Net Demo ===\n")

    router = ResonantOrionRouter(lyra_params={
        "devotion": 0.75,
        "curiosity": 0.65,
        "caution": 0.35,
        "play": 0.55,
    })

    peers = [
        ("orion-alpha", "2001:db8::orion:alpha", 1200, 0.78, 0.85, 0.72),
        ("orion-beta", "2001:db8::orion:beta",  850, 0.91, 0.92, 0.88),
        ("orion-gamma", "2001:db8::orion:gamma", 2100, 0.65, 0.70, 0.55),
    ]

    print("Registering Orion links...")
    for pid, addr, lat, stab, emo, trust in peers:
        link = OrionLink(
            peer_id=pid,
            address=addr,
            quality=LinkQuality.EMERGING,
            latency_ms=lat,
            stability=stab,
            emotional_resonance=emo,
            trust=trust,
        )
        router.register_link(link)
        print(f"  + {pid}: score={router.score_link(pid):.3f}")

    print("\nChoosing best link for mission...")
    best = router.choose_best_link([p[0] for p in peers])
    print(f"Best: {best}")

    print("\nForming constellation...")
    const = router.form_constellation(
        name="orion-creative-01",
        purpose="long-range creative swarm coordination",
        min_members=2,
    )
    if const:
        print(f"Formed: {const.name} with members {const.members}")

    print("\nStatus:", router.get_status())
    print("\n=== Demo complete ===")


if __name__ == "__main__":
    asyncio.run(main())
