# ST-014: Modèle JournalEntry et tagging

**Titre:** Journal avec notes/tags par trade

**User Story:** En tant que développeur backend, je veux associer journal à trades.

**Critères d'acceptation:**
- [ ] JournalEntry {tradeId, tags[], notes}
- [ ] POST/PUT /api/v1/journal/:tradeId

**Tâches techniques:**
- Relation Trade -> JournalEntry
- Tags as array PostgreSQL

**Estimation:** 2

**Dépendances:** ST-013

**Priority:** Must
