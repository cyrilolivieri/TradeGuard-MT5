# ST-007: Modèles PropChallenge et Rule

**Titre:** DB models pour challenges prop firms et règles

**User Story:** En tant que développeur backend, je veux modéliser les challenges et règles pour le rule engine.

**Critères d'acceptation:**
- [ ] PropChallenge { firm, phase, rules[] }
- [ ] Rule { type: 'DailyLoss', limit, current }
- [ ] Migration Prisma

**Tâches techniques:**
- Schema.prisma: PropChallenge, Rule
- Enums pour types règles (DailyLoss, MaxDD, ProfitTarget)
- Relations account -> challenges

**Estimation:** 2

**Dépendances:** ST-002, ST-005

**Priority:** Must
