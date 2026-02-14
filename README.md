# TradeGuard MT5

SaaS de trade management + journal analytics pour traders MetaTrader 5 avec conformité automatique aux règles des prop firms.

## 🎯 Vision

TradeGuard MT5 combine :
- **Conformité prop firm** : Prévention des violations de règles FTMO, FundedNext, etc.
- **Journal automatisé** : Capture automatique des trades avec screenshots et contexte marché
- **Analytics intelligent** : Pattern recognition et métriques de performance

## 🏗️ Architecture

| Couche | Technologie |
|--------|-------------|
| Frontend | Next.js 14 + TypeScript + Tailwind CSS |
| Backend | FastAPI (Python) + PostgreSQL |
| Real-time | WebSockets |
| MT5 Bridge | ZeroMQ + MQL5 EA |
| Deploy | Vercel + Railway |

## 📚 Documentation BMad

- [01 - Brainstorm](bmad/01-brainstorm.md)
- [02 - Brief](bmad/02-brief.md)
- [03 - PRD](bmad/03-prd.md)
- [04 - Architecture](bmad/04-architecture.md)
- [Stories](bmad/stories/)

## 🚀 Démarrage rapide

```bash
# Clone
git clone https://github.com/cyrilolivieri/TradeGuard-MT5.git
cd TradeGuard-MT5

# Backend
cd backend
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload

# Frontend (autre terminal)
cd frontend
npm install
npm run dev
```

## 📝 License

MIT
