# ST-001: Initialisation de la structure projet (Backend et Frontend)

**Titre:** Setup initial du monorepo Next.js + FastAPI

**User Story:** En tant que développeur backend/frontend, je veux initialiser la structure du projet pour démarrer le développement local.

**Critères d'acceptation:**
- [ ] Dossiers backend/ et frontend/ créés avec package.json initiaux
- [ ] Docker Compose pour Postgres + Redis fonctionnel
- [ ] `npm run dev` et `uvicorn` lancent sans erreur
- [ ] README.md avec instructions locales

**Tâches techniques:**
- Créer monorepo avec TurboRepo ou Nx (optionnel, simple dirs suffisent)
- Backend: `pip install fastapi uvicorn sqlalchemy alembic prisma[client] celery redis`
- Frontend: `npx create-next-app@14 frontend --ts --tailwind --eslint --app`
- Ajouter shadcn/ui: `npx shadcn-ui@latest init`
- Docker-compose.yml: Postgres, Redis
- .env.example avec vars requises
- Git init + .gitignore

**Estimation:** 3

**Dépendances:** Aucune

**Priority:** Must
