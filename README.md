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

This demo now runs a 18-step simulation with:
- More peers (7)
- Stronger failure penalties + mission success feedback that boosts the *whole* constellation
- Controlled randomness (RANDOM_SEED at top)
- Rich bar charts (scores, loyalty, energy) per step
- [Nexus] and [Solnet] ecosystem wiring inside the loop

For the richest experience, also install the Lyra emotional state machine:

```bash
pip install -e "git+https://github.com/digitaldesignerjazz/Nexus-Hyperspace-Lyra-1.0.git#egg=nexus-hyperspace-lyra"
```

The ResonantOrionRouter now accepts `state_machine=lyra_sm_instance` for fully dynamic, event-driven emotional modulation of link scores and routing decisions.

## Combined Ecosystem Runner

See `examples/nova_mini_cluster.py` for a small "start the next piece" combined runner that spins up a mini Nexus + Solnet + Orion + Lyra cluster simulation (gracefully mocks missing pieces).

## 🔍 Status & Roadmap

**Active Development**:
- Dramatic emotional drift simulation
- Rich visualization
- Ecosystem mock integrations
- Nova mini-cluster launcher

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
