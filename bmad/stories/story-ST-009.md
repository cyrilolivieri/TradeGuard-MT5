# ST-009: Moteur de calcul compliance

**Titre:** Logique backend pour calculer consommation règles (daily loss, DD, etc.)

**User Story:** En tant que développeur backend, je veux calculer en temps réel la compliance pour alertes.

**Critères d'acceptation:**
- [ ] Fonction calc_compliance(challenge_id) → update Rule.current/status
- [ ] Support DailyLoss (sum today), MaxDD (peak-trough), ProfitTarget
- [ ] Unit tests 80% coverage

**Tâches techniques:**
- Queries Prisma pour trades/aggrégats
- Utils pour DD calc (high water mark)
- Background task Celery pour periodic calc

**Estimation:** 5

**Dépendances:** ST-007, ST-008

**Priority:** Must
