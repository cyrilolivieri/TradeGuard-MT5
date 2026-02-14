# ST-020: Setup ZeroMQ bridge backend

**Titre:** Serveur ZeroMQ pour comm MT5

**User Story:** En tant que développeur backend, je veux ZMQ pour intégrer EA.

**Critères d'acceptation:**
- [ ] REQ/REP sockets sur port 5555
- [ ] Endpoint /bridge/status → ping MT5

**Tâches techniques:**
- pip install pyzmq
- Background thread ZMQ listener
- Messages: trade_sync, execute_order

**Estimation:** 3

**Dépendances:** ST-001, ST-013

**Priority:** Must
</xai:function_call name="write">
<parameter name="path">/home/cyril/.openclaw/workspace/projects/TradeGuard-MT5/bmad/stories/story-ST-021.md