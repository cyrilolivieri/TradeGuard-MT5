# Product Requirements Document (PRD)

## TradeGuard MT5

**Version:** 1.0  
**Date:** 2026-02-14  
**Status:** Draft

---

## 1. Overview & Objectives

### Vision
TradeGuard MT5 est un SaaS qui combine la conformité automatique aux règles des prop firms avec le journal de trading intelligent pour les utilisateurs de MetaTrader 5.

### Objectifs
- Prévenir 90%+ des violations de règles prop firm
- Automatiser la capture du journal (sauvegarder 5-10h/semaine)
- Fournir des analytics en temps réel sur les risques

### KPIs
- Taux de violation prévenu : >90%
- Temps économisé : 5+ heures/semaine par trader
- Adoption journal : >70% des utilisateurs actifs

---

## 2. Modules & User Stories

### Module 1: Authentification & Comptes

**US-001:** En tant que trader, je veux créer un compte avec email/mot de passe pour accéder à la plateforme.

**US-002:** En tant qu'utilisateur, je veux connecter mon compte MT5 pour synchroniser mes trades.

**US-003:** En tant qu'utilisateur, je veux gérer plusieurs comptes MT5 (personnel, prop firm) depuis un seul dashboard.

### Module 2: Rule Engine (Prop Firm Compliance)

**US-004:** En tant que trader prop firm, je veux sélectionner ma firme (FTMO, FundedNext, etc.) pour charger les règles automatiquement.

**US-005:** En tant qu'utilisateur, je veux voir en temps réel ma consommation des limites (daily loss, max drawdown, profit target).

**US-006:** En tant que trader, je veux recevoir des alertes avant de violer une règle (seuils configurables à 70%, 80%, 90%).

**US-007:** En tant qu'utilisateur, je veux que les trades bloquants soient rejetés avant exécution (pre-trade validation).

### Module 3: Journal Automatisé

**US-008:** En tant que trader, je veux que tous mes trades soient capturés automatiquement avec screenshot et contexte marché.

**US-009:** En tant qu'utilisateur, je veux ajouter des tags et notes à chaque trade pour mon analyse.

**US-010:** En tant que trader, je veux voir des statistiques sur mes performances (win rate, profit factor, expectancy) par stratégie/tag.

### Module 4: Analytics & Reporting

**US-011:** En tant qu'utilisateur, je veux un dashboard avec mes métriques clés (PnL, drawdown, trades/jour, etc.).

**US-012:** En tant que trader, je veux exporter mes données journal en CSV/PDF pour analyse externe.

**US-013:** En tant qu'utilisateur, je veux identifier mes patterns de trading (meilleures heures, meilleurs setups) via analytics.

### Module 5: EA Bridge

**US-014:** En tant que développeur EA, je veux envoyer des signaux webhook à TradeGuard pour exécution sur MT5.

**US-015:** En tant qu'utilisateur, je veux voir l'état de santé de mon bridge (latence, uptime, dernière synchronisation).

**US-016:** En tant que trader, je veux que le bridge vérifie les règles avant d'exécuter les ordres EA.

---

## 3. Technical Stack

- **Frontend:** Next.js 14 + TypeScript + Tailwind CSS + shadcn/ui
- **Backend:** FastAPI (Python) + PostgreSQL + Redis
- **Real-time:** WebSockets pour données temps réel
- **MT5 Integration:** ZeroMQ + MQL5 EA personnalisé
- **Auth:** JWT + NextAuth.js
- **Deployment:** Vercel (frontend) + Railway (backend)

---

## 4. Non-Functional Requirements

- **Performance:** Dashboard chargement < 2s, WebSocket latence < 100ms
- **Security:** JWT auth, HTTPS uniquement, données chiffrées au repos
- **Scalabilité:** Architecture stateless, horizontal scaling ready
- **Reliability:** 99.9% uptime, retry automatique sur erreurs MT5
- **Compliance:** GDPR ready, données utilisateurs exportables/supprimables

---

## 5. Timeline & Milestones

### Phase 1: MVP (6-8 semaines)
- Semaine 1-2: Setup projet, auth, connexion MT5 de base
- Semaine 3-4: Rule engine basique (FTMO + FundedNext), dashboard risques
- Semaine 5-6: Journal automatique, tags, analytics basiques
- Semaine 7-8: Tests, polish, déploiement beta

### Phase 2: Post-MVP (2-3 mois)
- +10 prop firms supportées
- EA Bridge avancé
- Analytics ML (pattern recognition)
- Mobile PWA

---

## 6. Out of Scope (pour MVP)

- Support MT4 (legacy, marché déclinant)
- Trading social / copy-trading
- Intégrations broker direct (hors MT5)
- Application mobile native (PWA suffisante)

---

*Document généré via BMad Method v5 - TradeGuard MT5 Project*
