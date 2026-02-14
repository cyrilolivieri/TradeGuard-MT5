# ST-019: Patterns basiques analytics

**Titre:** Meilleures heures/setups stats

**User Story:** En tant que développeur backend, je veux identifier patterns trading.

**Critères d'acceptation:**
- [ ] GET /api/v1/analytics/patterns → {hour_winrate, symbol_pf}

**Tâches techniques:**
- Group by HOUR(openTime), symbol
- Simple aggrégats

**Estimation:** 3

**Dépendances:** ST-016

**Priority:** Could
