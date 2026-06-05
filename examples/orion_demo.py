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
import random
from orion_net import OrionLink, ResonantOrionRouter, LinkQuality

# Optional: try to use the real Lyra state machine if available in the environment
try:
    from nexus_hyperspace_lyra.emotional_state_machine import LyraEmotionalStateMachine, PersonalityTraits
    HAS_LYRA_SM = True
except Exception:
    HAS_LYRA_SM = False


async def main():
    print("=== Orion Net — Time-Stepped Emotional Simulation ===\n")

    state_machine = None
    if HAS_LYRA_SM:
        print("LyraEmotionalStateMachine detected — running dynamic resonant simulation!\n")
        state_machine = LyraEmotionalStateMachine(
            agent_id="orion-router-1",
            personality=PersonalityTraits(
                energy_baseline=0.82,
                curiosity_factor=0.68,
                devotion_factor=0.72,
                collaboration_boost=0.14,
                failure_penalty=0.20,
            ),
            initial_energy=0.85,
        )
    else:
        print("Using static lyra_params (full dynamic behavior requires the LyraEmotionalStateMachine)\n")

    router = ResonantOrionRouter(
        lyra_params={
            "devotion": 0.72,
            "curiosity": 0.65,
            "caution": 0.38,
            "play": 0.52,
        },
        state_machine=state_machine,
    )

    peers = [
        ("orion-alpha", "2001:db8::orion:alpha", 1200, 0.78, 0.85, 0.72),
        ("orion-beta", "2001:db8::orion:beta",  850, 0.91, 0.92, 0.88),
        ("orion-gamma", "2001:db8::orion:gamma", 2100, 0.65, 0.70, 0.55),
    ]

    print("Registering Orion links (initial emotional resonance values)...")
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

    print("\n" + "="*70)
    print("Starting 15-step resonant simulation")
    print("="*70 + "\n")

    for step in range(1, 16):
        print(f"--- Step {step:02d} ---")

        if state_machine:
            # Apply random experiences
            num_events = random.randint(1, 2)
            for _ in range(num_events):
                peer = random.choice([p[0] for p in peers])
                if random.random() < 0.75:  # mostly positive collaborations
                    success = random.random() > 0.18
                    intensity = random.uniform(0.7, 1.35)
                    state_machine.process_event(
                        "collaboration" if success else "task_failure",
                        peer_id=peer,
                        success=success,
                        intensity=intensity
                    )
                    event_str = f"collaboration with {peer}" if success else f"failure on {peer}"
                else:
                    # occasional "discovery" event (boosts curiosity / energy slightly)
                    state_machine.process_event("discovery", intensity=0.8)
                    event_str = "new peer discovery / exploration"
                print(f"  Event: {event_str}")

            # Natural decay
            state_machine.decay(time_delta=random.uniform(0.8, 1.4))

        # Re-evaluate everything using current emotional state
        current_scores = {}
        for pid, _ in peers:
            current_scores[pid] = router.score_link(pid)

        # Choose best link this step
        best = router.choose_best_link([p[0] for p in peers])

        # Re-form constellation(s) — we keep one main one for visibility
        const = router.form_constellation(
            name="orion-main-constellation",
            purpose="ongoing resonant coordination",
            min_members=2,
        )

        if state_machine:
            report = state_machine.get_state_report()
            print(f"  Energy: {report['energy']:.3f}  |  Fatigue: {report['fatigue']:.3f}")
            loy = report.get('loyalty_map', {})
            if loy:
                print(f"  Loyalty map: " + ", ".join(f"{k}:{v:.2f}" for k,v in sorted(loy.items())))
        else:
            print(f"  (static mode)")

        print(f"  Current scores: " + ", ".join(f"{pid}:{score:.3f}" for pid, score in sorted(current_scores.items())))
        print(f"  Best link this step: {best}")

        if const:
            print(f"  Constellation members: {const.members}")
        else:
            print("  No viable constellation this step.")

        print()

    print("="*70)
    print("Simulation complete — observe how emotional state drifts routing & group formation.")
    print("="*70)

    if state_machine:
        final = state_machine.get_state_report()
        print(f"\nFinal emotional state: energy={final['energy']:.3f}, fatigue={final['fatigue']:.3f}")
        loy = final.get('loyalty_map', {})
        if loy:
            print(f"Final loyalty map: {loy}")

    print("\nRouter status:", router.get_status())
    print("\n=== Demo complete ===")


if __name__ == "__main__":
    asyncio.run(main())
