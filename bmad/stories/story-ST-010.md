# ST-010: WebSocket pour compliance temps réel

**Titre:** WS connection pour push updates compliance/alerts

**User Story:** En tant que développeur backend, je veux broadcaster compliance via WS pour dashboard live.

**Critères d'acceptation:**
- [ ] WS endpoint /ws/compliance
- [ ] Client subscribe:challenge {challengeId}
- [ ] Server → compliance:alert {rule, severity}

**Tâches techniques:**
- FastAPI WebSocket + Redis Pub/Sub
- Auth WS via JWT query param
- Background publisher sur compliance changes

**Estimation:** 5

**Dépendances:** ST-003, ST-009

**Priority:** Must
