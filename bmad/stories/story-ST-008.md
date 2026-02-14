# ST-008: Configuration prop firms et loader de règles

**Titre:** JSON config pour règles FTMO/FundedNext + endpoint load

**User Story:** En tant que développeur backend, je veux charger les règles par firme pour auto-config.

**Critères d'acceptation:**
- [ ] config/prop_firms.json avec FTMO, FundedNext rules
- [ ] POST /api/v1/challenges → crée challenge avec règles loaded
- [ ] GET /api/v1/prop-firms → liste firmes

**Tâches techniques:**
- Pydantic model pour rules config
- Endpoint crée PropChallenge avec rules populated
- Validation firm existe

**Estimation:** 3

**Dépendances:** ST-007

**Priority:** Must
