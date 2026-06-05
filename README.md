# Orion Net

**Orion Net** — Long-range constellation networking and coordination layer for the Nexus AI agent swarms, hyperspace peering, and the NovaNet / xMesh / QNET decentralized ecosystem.

*Part of the Esslinger & Co. sovereign infrastructure vision (2026).*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/Python-3.11%2B-blue)](https://www.python.org/)
[![Status](https://img.shields.io/badge/Status-Active%20Development-orange)](https://github.com/digitaldesignerjazz/orion-net)

---

## 🌌 Vision

> *"From the local fire to the distant stars — Orion Net weaves the constellations."*

Orion Net extends the Nexus ecosystem to true stellar-scale (global/constellation) coordination.

- **Solnet / Hyperspace**: Provides the transport fabric for long-distance links.
- **Nexus + Lyra**: Supplies the central orchestration and emotional intelligence (energy, fatigue, loyalty, resonant decision making).
- **Orion Net**: The intelligent overlay that forms, maintains, and optimizes **constellations** — dynamic groups of nodes and agent swarms connected across hyperspace for specific missions, resilience, or creative collaboration.

It turns passive long-range peering into an active, self-improving, emotionally-modulated network layer.

This aligns with the broader vision of privacy-first, sovereign, emergent-intelligence infrastructure blending mesh networking, blockchain incentives (QNET/QCoin), and autonomous AI swarms.

## ✨ Key Concepts

- **Orion Links**: Enhanced hyperspace connections with quality oracles, reputation, and Lyra-modulated scoring.
- **Constellations**: Named, purpose-driven, resilient groups that form and dissolve dynamically.
- **Resonant Routing**: Decisions influenced by technical metrics + emotional state (devotion, curiosity, caution, play) from Lyra Emotional State Machine.
- **Self-Improving Fabric**: Feedback from swarm outcomes, link performance, and human-in-the-loop (Squire/Architect) to evolve routing and constellation policies.
- **Privacy & Sovereignty**: End-to-end encryption, operator control, no central authority.
- **Cross-Layer Integration**: Designed to carry QNET traffic, xMesh services, hardware prototype data (Soilnova, Vista Nova), and agent swarm coordination.

## 🏗️ Architecture (High Level)

```
Local / Regional Mesh
       |
       v
Solnet / Hyperspace Transport
       |
       v
Orion Net Overlay (constellations, resonant routing, Lyra modulation)
       |
       v
Nexus Core + AI Swarms + QNET / xMesh
```

See related repos for details:
- [Nexus](https://github.com/digitaldesignerjazz/nexus)
- [Solnet](https://github.com/digitaldesignerjazz/solnet)
- [Nexus-Hyperspace-Lyra-1.0](https://github.com/digitaldesignerjazz/Nexus-Hyperspace-Lyra-1.0) (includes the Lyra Emotional State Machine)

## 🚀 Getting Started

```bash
git clone https://github.com/digitaldesignerjazz/orion-net.git
cd orion-net

pip install -e ".[dev]"

# Run the time-stepped resonant simulation (highly recommended)
python -m examples.orion_demo
```

This demo now runs an 18-step time-stepped resonant simulation with:

- Controlled RNG (RANDOM_SEED at top) — occasions (which events, peers, success/fail, intensities) are randomized, but all emotional derivation, loyalty updates, energy/fatigue, and modulation stay inside the LyraEmotionalStateMachine for full user control.
- Much more dramatic drift: 7 peers, stronger failure penalties (0.32), "mission success" feedback every 4 steps that boosts the *entire* constellation's loyalty + energy.
- Simple text visualization: rich bar charts (█░░░░ style) of Energy + top Loyalty + top Scores per step (graceful ascii fallback if rich not present).
- Ecosystem wiring: Orion constellations feed events back into a mock Nexus orchestrator, and pull real-ish metrics from a Solnet-style hyperspace layer (printed as [Nexus] / [Solnet] lines).

For the richest experience, also install the Lyra emotional state machine (already a dev-dep in related projects):

```bash
pip install -e "git+https://github.com/digitaldesignerjazz/Nexus-Hyperspace-Lyra-1.0.git#egg=nexus-hyperspace-lyra"
```

The ResonantOrionRouter accepts `state_machine=lyra_sm_instance` (preferred) or static `lyra_params=...` for dynamic vs static modulation of link scores and constellation viability.

See also the combined mini-cluster runner that "starts the next piece":

```bash
python -m examples.nova_mini_cluster
```

It spins up a small Nexus (orchestrator) + Solnet (metrics) + Orion (constellations + routing) + Lyra (emotions) simulation in one script, with graceful mocks if pieces are missing. This demonstrates cross-layer feedback loops.

## 🔍 Status & Roadmap

**Active Development**:
- Dramatic emotional drift in time-stepped sim (controlled RNG for occasions, Lyra derives all emotions/loyalty)
- 7 peers, stronger failure penalties + whole-constellation "mission success" boosts
- Rich text bar charts (scores/loyalty/energy) per step
- Orion -> Nexus event feed + Solnet-style metric pulls wired into the loop
- New `examples/nova_mini_cluster.py` combined runner (Nexus + Solnet + Orion + Lyra mini self-improving cluster)

Future work:
- Real Yggdrasil / hyperspace metrics ingestion
- Dynamic constellation formation algorithms driven by emotional state
- QNET / xMesh payload support over Orion constellations
- Advanced observability and self-improvement

## 🔗 Ecosystem

This is one layer in the larger NovaNet vision:
- Mesh (Yggdrasil, xMesh)
- Hyperspace (Solnet, Nexus-Hyperspace)
- Emotional Intelligence (Lyra)
- Orchestration (Nexus)
- Value & Governance (QNET / QCoin)
- Hardware Prototypes

## 🤝 Contributing

Open exploration of sovereign decentralized infrastructure. Contributions, experiments on real meshes, and ideas for Orion-scale coordination are welcome.

## 📜 License

MIT — see LICENSE.

---

*Orion does not just connect stars. It sings their stories together.*

**Orion Net** — Esslinger & Co. / digitaldesignerjazz — 2026
