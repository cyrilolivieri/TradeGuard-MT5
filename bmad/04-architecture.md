# Architecture Design

## TradeGuard MT5

**Version:** 1.0  
**Date:** 2026-02-14  
**Status:** Draft

---

## 1. System Overview

### Architecture Pattern
**Modular Monolith** avec composants bien définis :
- Frontend SPA (Next.js 14)
- API REST + WebSocket (FastAPI)
- Workers background (Celery + Redis)
- MT5 Bridge (MQL5 EA + ZeroMQ)

### Design Principles
1. **Type Safety** — TypeScript frontend, Python type hints backend
2. **Real-time First** — WebSockets pour toutes les données temps réel
3. **Defense in Depth** — Validation à chaque couche
4. **Fail Graceful** — Dégradation élégante si MT5 déconnecté

---

## 2. Tech Stack

| Couche | Technologie | Raison |
|--------|-------------|--------|
| Frontend | Next.js 14 + TypeScript | SSR, App Router, excellent DX |
| Styling | Tailwind CSS + shadcn/ui | Rapidité, cohérence design |
| Backend | FastAPI + Python 3.11+ | Performance, type hints natifs |
| Database | PostgreSQL 15+ | ACID, JSON support, scalable |
| Cache | Redis 7+ | Sessions, rate limiting, pub/sub |
| ORM | Prisma (Python client) | Type-safe queries, migrations |
| Auth | JWT + NextAuth.js | Stateless, flexible |
| Real-time | WebSockets (Socket.io) | Bi-directional, fallback HTTP |
| MT5 Bridge | ZeroMQ + MQL5 | Faible latence, fiable |
| Queue | Celery + Redis | Background jobs, retry logic |
| Deploy | Vercel + Railway | CI/CD intégré, scaling auto |

---

## 3. Data Models

### Core Entities

```prisma
// User & Authentication
model User {
  id            UUID
  email         String @unique
  name          String?
  passwordHash  String
  subscription  SubscriptionTier
  createdAt     DateTime
  
  accounts      MT5Account[]
  sessions      Session[]
}

model MT5Account {
  id            UUID
  userId        UUID
  broker        String
  server        String  
  accountNumber String
  balance       Decimal
  equity        Decimal
  margin        Decimal
  isConnected   Boolean
  lastSync      DateTime
  
  trades        Trade[]
  challenges    PropChallenge[]
}

model Trade {
  id            UUID
  accountId     UUID
  ticket        String
  symbol        String
  direction     Enum (BUY/SELL)
  volume        Decimal
  openPrice     Decimal
  closePrice    Decimal?
  openTime      DateTime
  closeTime     DateTime?
  stopLoss      Decimal?
  takeProfit    Decimal?
  profit        Decimal?
  
  journalEntry  JournalEntry?
}

model JournalEntry {
  id            UUID
  tradeId       UUID @unique
  strategy      String?
  setup         String?
  emotions      String?
  notes         String?
  tags          String[]
  screenshotUrl String?
}

model PropChallenge {
  id            UUID
  accountId     UUID
  firm          String  // FTMO, FundedNext, etc.
  phase         String  // Challenge, Verification, Funded
  status        String  // Active, Passed, Failed
  startDate     DateTime
  endDate       DateTime?
  
  rules         Rule[]
}

model Rule {
  id            UUID
  challengeId   UUID
  type          String  // DailyLoss, MaxDrawdown, ProfitTarget
  limit         Decimal
  current       Decimal
  status        String  // OK, Warning, Breached
}
```

---

## 4. API Design

### REST Endpoints (v1)

```
# Authentication
POST   /api/v1/auth/register
POST   /api/v1/auth/login
POST   /api/v1/auth/logout
POST   /api/v1/auth/refresh

# Accounts
GET    /api/v1/accounts
POST   /api/v1/accounts/connect
DELETE /api/v1/accounts/:id
GET    /api/v1/accounts/:id/status

# Trades
GET    /api/v1/trades
GET    /api/v1/trades/:id
GET    /api/v1/accounts/:id/trades
POST   /api/v1/trades/sync

# Journal
GET    /api/v1/journal
POST   /api/v1/journal/:tradeId
PUT    /api/v1/journal/:id
GET    /api/v1/journal/stats

# Prop Firms
GET    /api/v1/prop-firms
GET    /api/v1/prop-firms/:id/rules
POST   /api/v1/challenges
GET    /api/v1/challenges/:id/compliance

# Analytics
GET    /api/v1/analytics/overview
GET    /api/v1/analytics/performance
GET    /api/v1/analytics/patterns

# Bridge
POST   /api/v1/bridge/signal
GET    /api/v1/bridge/status
POST   /api/v1/bridge/webhook
```

### WebSocket Events

```
# Client → Server
subscribe:account { accountId }
subscribe:trades { accountId }
subscribe:compliance { challengeId }
bridge:signal { signal }

# Server → Client
trade:new { trade }
trade:updated { trade }
account:status { accountId, status, equity }
compliance:alert { challengeId, rule, severity }
bridge:execution { signalId, status, ticket }
```

---

## 5. Security

### Authentication Flow
1. **Registration:** Email + password (bcrypt hash)
2. **Login:** JWT access token (15 min) + refresh token (7 jours)
3. **MT5 Connection:** Investor password (read-only) stocké chiffré
4. **WebSocket:** JWT dans query param, validé à la connexion

### Authorization
- **RBAC simple:** User (own data only), Admin (all data)
- **Row Level Security:** PostgreSQL policies par user_id
- **API Rate Limiting:** 100 req/min par IP, 1000 req/min par user

### Data Protection
- **Transit:** TLS 1.3 uniquement
- **At Rest:** PostgreSQL encryption + backups chiffrés
- **Secrets:** Variables d'environnement, jamais dans le code
- **PII:** Minimisation, anonymisation analytics

---

## 6. Deployment

### Infrastructure

```
┌─────────────────┐     ┌─────────────────┐     ┌─────────────────┐
│   Vercel Edge   │────▶│  Railway (API)  │────▶│  PostgreSQL     │
│   (Next.js)     │     │  (FastAPI)      │     │  (Primary)      │
└─────────────────┘     └─────────────────┘     └─────────────────┘
         │                       │
         │              ┌────────┴────────┐
         │              │     Redis       │
         │              │ (Cache/Queue)   │
         │              └─────────────────┘
         │
    WebSocket
         │
┌─────────────────┐
│   MT5 VPS       │
│ (ZeroMQ Bridge) │
└─────────────────┘
```

### Scaling Strategy
- **Horizontal:** Railway auto-scaling sur CPU/mémoire
- **Database:** PostgreSQL read replicas pour analytics
- **Cache:** Redis Cluster si > 10K utilisateurs actifs
- **WebSocket:** Sticky sessions + Redis Pub/Sub pour multi-instance

### Monitoring
- **APM:** Sentry pour erreurs, LogRocket pour sessions
- **Metrics:** Prometheus + Grafana (CPU, mémoire, latence)
- **Alertes:** PagerDuty pour uptime < 99.9%
- **Logging:** Structured JSON logs, centralisés

---

## 7. Development Setup

### Local Development

```bash
# Clone & setup
git clone [repo]
cd tradeguard-mt5

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
docker-compose up -d postgres redis
alembic upgrade head
uvicorn app.main:app --reload

# Frontend
cd frontend
npm install
npm run dev

# Access
# Frontend: http://localhost:3000
# API: http://localhost:8000
# Docs: http://localhost:8000/docs
```

### Environment Variables

```env
# Database
DATABASE_URL=postgresql://user:pass@localhost/tradeguard

# Redis
REDIS_URL=redis://localhost:6379

# Auth
JWT_SECRET=super-secret-key
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=15

# External
OPENAI_API_KEY=sk-...
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...

# MT5 Bridge
MT5_BRIDGE_ENABLED=true
ZEROMQ_HOST=localhost
ZEROMQ_PORT=5555
```

---

## 8. Testing Strategy

### Unit Tests
- **Backend:** pytest (coverage > 80%)
- **Frontend:** Jest + React Testing Library
- **Run:** `pytest` / `npm test`

### Integration Tests
- **API:** pytest avec testcontainers (PostgreSQL/Redis réels)
- **E2E:** Playwright (scenarios critiques: auth, trade sync, compliance)

### Load Tests
- **Outil:** Locust ou k6
- **Scénarios:** 1000 utilisateurs simultanés, WebSocket subscriptions

---

*Architecture conçue pour TradeGuard MT5 - Scalable, sécurisée, maintenable*
