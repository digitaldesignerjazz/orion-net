"""
Orion Net basic demo.

Shows link registration, Lyra-modulated scoring (static or via LyraEmotionalStateMachine),
and constellation formation.

Run: python -m examples.orion_demo

For full dynamic behavior, install the LyraEmotionalStateMachine from
https://github.com/digitaldesignerjazz/Nexus-Hyperspace-Lyra-1.0 and pass
an instance as state_machine=...
"""

import asyncio
from orion_net import OrionLink, ResonantOrionRouter, LinkQuality

# Optional: try to use the real Lyra state machine if available in the environment
try:
    from nexus_hyperspace_lyra.emotional_state_machine import LyraEmotionalStateMachine, PersonalityTraits
    HAS_LYRA_SM = True
except Exception:
    HAS_LYRA_SM = False


async def main():
    print("=== Orion Net Demo ===\n")

    state_machine = None
    if HAS_LYRA_SM:
        print("LyraEmotionalStateMachine detected - using dynamic emotional state!")
        state_machine = LyraEmotionalStateMachine(
            agent_id="orion-router-1",
            personality=PersonalityTraits(
                energy_baseline=0.85,
                curiosity_factor=0.70,
                devotion_factor=0.75,
            ),
            initial_energy=0.88,
        )
        # Simulate some "experiences" before routing
        state_machine.process_event("collaboration", peer_id="orion-beta", success=True, intensity=1.1)
        state_machine.decay(time_delta=0.5)
        print("  (Simulated some emotional events for the state machine)")
    else:
        print("Using static lyra_params (install Nexus-Hyperspace-Lyra for full dynamic LyraEmotionalStateMachine)")

    router = ResonantOrionRouter(
        lyra_params={
            "devotion": 0.75,
            "curiosity": 0.65,
            "caution": 0.35,
            "play": 0.55,
        },
        state_machine=state_machine,
    )

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
