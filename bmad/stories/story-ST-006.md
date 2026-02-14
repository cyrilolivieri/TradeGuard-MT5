# ST-006: Dashboard Comptes Frontend

**Titre:** Liste et gestion comptes MT5 dans dashboard

**User Story:** En tant que développeur frontend, je veux afficher/gérer les comptes MT5 connectés.

**Critères d'acceptation:**
- [ ] Page /dashboard/accounts avec DataTable shadcn
- [ ] Bouton connect/disconnect
- [ ] Status (connected, balance stub)

**Tâches techniques:**
- Query API /accounts
- Tanstack Query pour caching
- Composants Table, Badge, Button
- Modal pour connect form

**Estimation:** 2

**Dépendances:** ST-004, ST-005

**Priority:** Must
