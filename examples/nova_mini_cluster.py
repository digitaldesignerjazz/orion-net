"""
Nova Mini-Cluster — Combined runner that spins up a small Nexus + Solnet + Orion + Lyra simulation.

This is the "next piece" — a lightweight launcher demonstrating how the pieces of the ecosystem
(Nexus orchestration, Solnet hyperspace metrics, Orion constellation networking, Lyra emotional state)
can work together in a mini self-improving cluster.

Run:
    python -m examples.nova_mini_cluster

It gracefully degrades if the other packages (nexus, solnet, nexus_hyperspace_lyra) are not installed.
"""

import random
import time

# --- Try to import real pieces from the ecosystem ---
try:
    from orion_net import OrionLink, ResonantOrionRouter, LinkQuality
    HAS_ORION = True
except Exception:
    HAS_ORION = False

try:
    from nexus_hyperspace_lyra.emotional_state_machine import LyraEmotionalStateMachine, PersonalityTraits
    HAS_LYRA = True
except Exception:
    HAS_LYRA = False

# Mocks for Nexus and Solnet (so the combined runner always works)
class MockNexusOrchestrator:
    def __init__(self):
        self.events = []

    def receive_constellation_event(self, const_name, members, emotional_summary, step):
        self.events.append((step, const_name, members, emotional_summary))
        print(f"[Nexus Orchestrator] Step {step}: Received from {const_name} | members={len(members)} | emotional={emotional_summary}")

class MockSolnetLayer:
    def pull_metrics(self, constellation):
        latency = random.uniform(700, 2400)
        stability = random.uniform(0.5, 0.97)
        print(f"[Solnet] Pulled hyperspace metrics for {constellation}: latency≈{latency:.0f}ms, stability={stability:.2f}")
        return {"latency": latency, "stability": stability}

def main():
    print("=== Nova Mini-Cluster — Combined Ecosystem Runner ===\n")
    print("Spinning up: Nexus (orchestrator) + Solnet (metrics) + Orion (constellations) + Lyra (emotions)\n")

    random.seed(123)  # controlled but interesting run

    # --- Initialize pieces ---
    solnet = MockSolnetLayer()
    nexus = MockNexusOrchestrator()

    state_machine = None
    if HAS_LYRA:
        state_machine = LyraEmotionalStateMachine(
            agent_id="nova-cluster-lyra",
            personality=PersonalityTraits(
                energy_baseline=0.81,
                failure_penalty=0.26,
                collaboration_boost=0.13,
            ),
            initial_energy=0.84,
        )
        print("Lyra emotional state machine: ACTIVE")
    else:
        print("Lyra emotional state machine: MOCK (static)")

    router = None
    if HAS_ORION:
        router = ResonantOrionRouter(
            lyra_params={"devotion": 0.71, "curiosity": 0.64, "caution": 0.39, "play": 0.51},
            state_machine=state_machine,
        )
        print("Orion Net router: ACTIVE")
    else:
        print("Orion Net router: MOCK")

    # Simple peers for the mini cluster
    peers = [
        ("node-1", "orion-1", 1100, 0.80, 0.83, 0.71),
        ("node-2", "orion-2",  920, 0.89, 0.91, 0.84),
        ("node-3", "orion-3", 1750, 0.71, 0.76, 0.64),
        ("node-4", "orion-4", 1400, 0.82, 0.79, 0.77),
    ]

    if router:
        for pid, addr, lat, stab, emo, trust in peers:
            link = OrionLink(pid, addr, latency_ms=lat, stability=stab, emotional_resonance=emo, trust=trust)
            router.register_link(link)
        print(f"Orion links registered: {len(peers)}")
    else:
        print(f"Mock peers active: {len(peers)}")

    print("\n--- Running 12 combined steps ---\n")

    for step in range(1, 13):
        print(f"Step {step:02d}:")

        # Orion / Lyra side
        if router and state_machine:
            # random experiences
            for _ in range(random.randint(1, 2)):
                peer = random.choice([p[0] for p in peers])
                success = random.random() > 0.25
                state_machine.process_event("collaboration" if success else "task_failure",
                                            peer_id=peer, success=success, intensity=random.uniform(0.8, 1.3))
            state_machine.decay(1.0)

            # mission success feedback to whole constellation
            if step % 3 == 0:
                const = router.form_constellation("nova-main", "combined cluster mission", min_members=2)
                if const:
                    print(f"  [Mission Success] Boosting constellation {const.members}")
                    for m in const.members:
                        state_machine.process_event("collaboration", peer_id=m, success=True, intensity=1.5)

            scores = {p[0]: router.score_link(p[0]) for p in peers}
            best = router.choose_best_link([p[0] for p in peers])
            const = router.form_constellation("nova-main", "combined cluster mission", min_members=2)

            print(f"  Orion best: {best} | constellation: {const.members if const else 'none'}")

            # Feed to Nexus
            if const:
                emotional = state_machine.get_state_report() if state_machine else {}
                nexus.receive_constellation_event(const.name, const.members, emotional, step)

            # Pull from Solnet
            solnet.pull_metrics("nova-main" if const else "none")

        else:
            # pure mock run
            if step % 3 == 0:
                print("  [Mission Success] (mock) boosting cluster energy")
            nexus.receive_constellation_event("nova-main", ["node-1","node-2"], {"energy": 0.9}, step)
            solnet.pull_metrics("nova-main")

        print()

    print("=== Mini-cluster run complete ===")
    print(f"Total Nexus events received: {len(nexus.events)}")
    print("The pieces are talking to each other. This is the beginning of the combined Nova system.")

if __name__ == "__main__":
    main()
