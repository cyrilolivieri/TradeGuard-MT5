# ST-002: Modèles de base base de données (User, Session)

**Titre:** Implémentation des modèles Prisma pour User et Session

**User Story:** En tant que développeur backend, je veux définir les modèles User et Session en Prisma pour gérer l'authentification.

**Critères d'acceptation:**
- [ ] `prisma/schema.prisma` avec User et Session
- [ ] `prisma migrate dev` crée les tables
- [ ] Alembic/SQLAlchemy compat si besoin
- [ ] Row Level Security basique sur user_id

**Tâches techniques:**
- Définir schema.prisma avec User { id, email, passwordHash, ... }
- Session { id, userId, token, expiresAt }
- `prisma generate` et `prisma db push`
- Seed script pour admin user
- Tests unitaires modèles

**Estimation:** 2

**Dépendances:** ST-001

**Priority:** Must
