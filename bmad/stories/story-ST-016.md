# ST-016: Stats journal basiques (winrate, PF)

**Titre:** Calcul stats par tag/stratégie

**User Story:** En tant que développeur backend, je veux stats journal pour analytics.

**Critères d'acceptation:**
- [ ] GET /api/v1/journal/stats?tags=scalping → {winrate, profitFactor}

**Tâches techniques:**
- Raw SQL ou Prisma aggrégats
- Cache Redis 5min

**Estimation:** 3

**Dépendances:** ST-014

**Priority:** Should
