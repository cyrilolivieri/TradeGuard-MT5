# ST-005: Modèle MT5Account et connexion basique

**Titre:** DB model pour comptes MT5 et endpoint connect

**User Story:** En tant que développeur backend, je veux modéliser les comptes MT5 pour stocker les creds chiffrés.

**Critères d'acceptation:**
- [ ] Modèle MT5Account { broker, server, accountNumber, investorPass (encrypted) }
- [ ] POST /api/v1/accounts/connect → stocke et teste connexion (stub pour MVP)
- [ ] GET /api/v1/accounts → liste comptes user

**Tâches techniques:**
- Ajouter MT5Account à schema.prisma
- Encryption creds (fernet ou pg crypto)
- Endpoint avec auth dependency
- Validation Pydantic

**Estimation:** 3

**Dépendances:** ST-002, ST-003

**Priority:** Must
