# ST-011: Validation pre-trade

**Titre:** API pour valider trade avant exécution

**User Story:** En tant que développeur backend, je veux rejeter trades qui violeraient règles.

**Critères d'acceptation:**
- [ ] POST /api/v1/compliance/validate-trade {symbol, volume, direction}
- [ ] Simulate impact sur rules → {approved, risks[]}

**Tâches techniques:**
- Simul calc loss/DD post-trade
- Intégration calc_compliance sim

**Estimation:** 3

**Dépendances:** ST-009

**Priority:** Must
