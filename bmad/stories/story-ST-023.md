# ST-023: Webhook signals pour EAs externes

**Titre:** Endpoint webhook pour signals EA

**User Story:** En tant que développeur backend, je veux recevoir signals webhook.

**Critères d'acceptation:**
- [ ] POST /api/v1/bridge/webhook → validate + forward ZMQ to EA
- [ ] Response {approved, ticket}

**Tâches techniques:**
- Signature HMAC validation
- Async ZMQ send to EA

**Estimation:** 3

**Dépendances:** ST-020, ST-011

**Priority:** Should
