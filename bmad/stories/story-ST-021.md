# ST-021: MQL5 EA basique avec ZeroMQ

**Titre:** Expert Advisor MT5 pour comm avec backend

**User Story:** En tant que développeur EA, je veux un EA stub qui sync trades via ZMQ.

**Critères d'acceptation:**
- [ ] EA compile, attache à chart
- [ ] OnTick() → send trade history ZMQ
- [ ] Receive validate_trade → approve/deny

**Tâches techniques:**
- MQL5 code: ZMQ library include
- REQ socket to backend:5555
- Serialize trades JSON

**Estimation:** 8

**Dépendances:** ST-020

**Priority:** Must
