# ST-013: Modèle Trade et sync endpoint

**Titre:** Capture trades MT5 (stub pour MVP)

**User Story:** En tant que développeur backend, je veux sync trades pour journal/compliance.

**Critères d'acceptation:**
- [ ] Trade model Prisma
- [ ] POST /api/v1/trades/sync {accountId, trades[] } → upsert
- [ ] Trigger compliance recalc

**Tâches techniques:**
- Schema Trade {ticket, symbol, volume, profit, ...}
- Bulk upsert Prisma
- Celery task pour sync

**Estimation:** 3

**Dépendances:** ST-005, ST-009

**Priority:** Must
