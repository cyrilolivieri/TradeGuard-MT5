# ST-018: Export CSV/PDF journal

**Titre:** Génération exports pour trades/journal

**User Story:** En tant que développeur backend/frontend, je veux exporter data.

**Critères d'acceptation:**
- [ ] GET /api/v1/trades/export?format=csv → download
- [ ] PDF via reportlab ou frontend jsPDF

**Tâches techniques:**
- Pandas to_csv ou streaming
- Celery pour gros exports

**Estimation:** 3

**Dépendances:** ST-013

**Priority:** Should
