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

# Control the randomness for reproducibility while allowing dramatic/emergent behavior
RANDOM_SEED = 42
random.seed(RANDOM_SEED)

# Optional: try to use the real Lyra state machine if available in the environment
try:
    from nexus_hyperspace_lyra.emotional_state_machine import LyraEmotionalStateMachine, PersonalityTraits
    HAS_LYRA_SM = True
except Exception:
    HAS_LYRA_SM = False

# Rich for visualization (dev dep)
try:
    from rich.console import Console
    from rich.table import Table
    console = Console()
    HAS_RICH = True
except Exception:
    HAS_RICH = False
    console = None

def print_emotion_bars(step, energy, loyalties, scores, width=25):
    """Simple text bar charts using rich or fallback ascii."""
    if HAS_RICH and console:
        table = Table(title=f"Step {step:02d} — Emotional & Score Drift")
        table.add_column("Metric", style="cyan", no_wrap=True)
        table.add_column("Bar", style="green")
        table.add_column("Value", style="magenta")

        # Energy
        filled = int(energy * width)
        bar = "█" * filled + "░" * (width - filled)
        table.add_row("Energy", bar, f"{energy:.2f}")

        # Top loyalties
        for i, (k, v) in enumerate(sorted(loyalties.items(), key=lambda x: -x[1])[:3]):
            filled = int(v * width)
            bar = "█" * filled + "░" * (width - filled)
            table.add_row(f"Loyalty {k}", bar, f"{v:.2f}")

        # Top scores
        for i, (k, v) in enumerate(sorted(scores.items(), key=lambda x: -x[1])[:3]):
            filled = int(v * width)
            bar = "█" * filled + "░" * (width - filled)
            table.add_row(f"Score {k}", bar, f"{v:.2f}")

        console.print(table)
    else:
        # Fallback
        print(f"  Energy: {'█'*int(energy*20)}{'░'*(20-int(energy*20))} {energy:.2f}")
        for k, v in list(sorted(loyalties.items(), key=lambda x:-x[1]))[:2]:
            print(f"  Loyalty {k}: {'█'*int(v*20)}{'░'*(20-int(v*20))} {v:.2f}")
        for k, v in list(sorted(scores.items(), key=lambda x:-x[1]))[:2]:
            print(f"  Score {k}: {'█'*int(v*20)}{'░'*(20-int(v*20))} {v:.2f}")


async def main():
    print("=== Orion Net — Time-Stepped Emotional Simulation ===\n")

    state_machine = None
    if HAS_LYRA_SM:
        print("LyraEmotionalStateMachine detected — running dynamic resonant simulation!\n")
        state_machine = LyraEmotionalStateMachine(
            agent_id="orion-router-1",
            personality=PersonalityTraits(
                energy_baseline=0.80,
                curiosity_factor=0.65,
                devotion_factor=0.70,
                collaboration_boost=0.12,
                failure_penalty=0.28,  # stronger penalties for more dramatic drift
            ),
            initial_energy=0.82,
        )
    else:
        print("Using static lyra_params (full dynamic behavior requires the LyraEmotionalStateMachine)\n")

    router = ResonantOrionRouter(
        lyra_params={
            "devotion": 0.70,
            "curiosity": 0.62,
            "caution": 0.40,
            "play": 0.50,
        },
        state_machine=state_machine,
    )

    # More peers for more dramatic interactions and complex loyalty graphs
    peers = [
        ("orion-alpha", "2001:db8::orion:alpha", 1200, 0.78, 0.82, 0.70),
        ("orion-beta", "2001:db8::orion:beta",   850, 0.92, 0.90, 0.85),
        ("orion-gamma", "2001:db8::orion:gamma", 2100, 0.68, 0.72, 0.60),
        ("orion-delta", "2001:db8::orion:delta", 1500, 0.85, 0.80, 0.75),
        ("orion-epsilon", "2001:db8::orion:eps", 950, 0.75, 0.88, 0.82),
        ("orion-zeta", "2001:db8::orion:zeta",  1800, 0.70, 0.78, 0.65),
        ("orion-eta", "2001:db8::orion:eta",    1350, 0.88, 0.85, 0.78),
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

    print("\n" + "="*75)
    print("Starting 18-step resonant simulation — watch the emotional drift!")
    print("="*75 + "\n")

    for step in range(1, 19):
        print(f"--- Step {step:02d} ---")

        if state_machine:
            # Apply random experiences (more occasions for dramatic emotions, controlled by seed)
            num_events = random.randint(1, 3)
            for _ in range(num_events):
                peer = random.choice([p[0] for p in peers])
                roll = random.random()
                if roll < 0.62:  # collaborations (positive drift)
                    success = random.random() > 0.22
                    intensity = random.uniform(0.65, 1.45)
                    state_machine.process_event(
                        "collaboration" if success else "task_failure",
                        peer_id=peer,
                        success=success,
                        intensity=intensity
                    )
                    event_str = f"collaboration with {peer}" if success else f"failure on {peer}"
                elif roll < 0.82:
                    state_machine.process_event("discovery", intensity=random.uniform(0.6, 1.15))
                    event_str = "new peer discovery / exploration"
                else:
                    # external stress for negative
                    state_machine.process_event("task_failure", peer_id=peer, success=False, intensity=1.35)
                    event_str = f"external stress on {peer}"
                print(f"  Event: {event_str}")

            # Natural decay
            state_machine.decay(time_delta=random.uniform(0.7, 1.5))

            # “mission success” feedback that boosts the whole constellation’s loyalty/energy (dramatic positive)
            if step % 4 == 0:
                const_now = router.form_constellation(
                    name="orion-main-constellation",
                    purpose="ongoing resonant coordination",
                    min_members=2,
                )
                if const_now and state_machine:
                    print(f"  [Mission Success] Boosting entire constellation's loyalty/energy!")
                    for member in const_now.members:
                        state_machine.process_event("collaboration", peer_id=member, success=True, intensity=1.7)

        # Re-evaluate everything using current emotional state
        current_scores = {}
        for p in peers:
            pid = p[0]
            current_scores[pid] = router.score_link(pid)

        # Choose best link this step
        best = router.choose_best_link([p[0] for p in peers])

        # Re-form constellation
        const = router.form_constellation(
            name="orion-main-constellation",
            purpose="ongoing resonant coordination",
            min_members=2,
        )

        # === Wire in more of the ecosystem (mock Nexus orchestrator + Solnet layer) ===
        if const:
            # Feed events back into a Nexus orchestrator
            print(f"  [Nexus] Orion constellation '{const.name}' feeding emotional event back to orchestrator "
                  f"(members={len(const.members)}, best_link={best})")

            # Pull real-ish metrics from a Solnet-style layer
            solnet_latency = random.uniform(750, 2300)
            solnet_stability = random.uniform(0.52, 0.96)
            print(f"  [Solnet] Pulled hyperspace metrics: avg_latency={solnet_latency:.0f}ms, stability={solnet_stability:.2f}")

        # Visualization with rich bars
        if state_machine:
            report = state_machine.get_state_report()
            energy = report['energy']
            loyalties = report.get('loyalty_map', {})
            print(f"  Energy: {energy:.3f}  |  Fatigue: {report['fatigue']:.3f}")
            print_emotion_bars(step, energy, loyalties, current_scores)
        else:
            print(f"  (static mode)")
            print_emotion_bars(step, 0.5, {}, current_scores)

        print(f"  Current scores: " + ", ".join(f"{pid}:{score:.3f}" for pid, score in sorted(current_scores.items(), key=lambda x:-x[1])[:4]))
        print(f"  Best link this step: {best}")

        if const:
            print(f"  Constellation members: {const.members}")
        else:
            print("  No viable constellation this step.")

        print()

    print("="*75)
    print("Simulation complete — the resonant / self-improving personality is now visible in the drift.")
    print("="*75)

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
