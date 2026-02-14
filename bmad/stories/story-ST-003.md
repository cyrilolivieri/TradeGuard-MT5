# ST-003: Endpoints d'authentification Backend (Register/Login)

**Titre:** API REST pour registration et login avec JWT

**User Story:** En tant que développeur backend, je veux implémenter les endpoints auth pour permettre l'inscription et connexion.

**Critères d'acceptation:**
- [ ] POST /api/v1/auth/register → crée user, retourne JWT
- [ ] POST /api/v1/auth/login → valide creds, retourne JWT access/refresh
- [ ] Erreurs 400/401/409 gérées
- [ ] Rate limiting sur login (Redis)

**Tâches techniques:**
- Dependencies: passlib, python-jose, bcrypt
- CRUD User avec Prisma
- JWT encode/decode utils
- Pydantic schemas pour requests/responses
- FastAPI dependencies pour auth

**Estimation:** 5

**Dépendances:** ST-001, ST-002

**Priority:** Must
