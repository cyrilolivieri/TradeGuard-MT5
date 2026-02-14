# TradeGuard MT5 - Project Brief

**Document Version:** 1.0  
**Date:** 2026-02-14  
**Status:** Draft for Review  
**Prepared By:** Business Analysis Team  

---

## 1. Executive Summary

TradeGuard MT5 is a SaaS platform that combines real-time prop firm compliance enforcement with automated trade journaling for MetaTrader 5 traders. By intercepting trades before execution and validating them against configurable rule sets, the platform prevents costly violations while capturing rich trading data for performance analytics. This addresses a critical gap in the market where traders currently rely on fragmented tools and manual monitoring to manage prop firm restrictions.

---

## 2. Problem Statement

- **High Violation Rates:** 30-40% of prop firm traders fail due to unintentional rule violations, resulting in account losses and wasted evaluation fees
- **Fragmented Tooling:** Serious traders use 5-7 separate tools (spreadsheets, calculators, journals, rule checkers) with no integration
- **Manual Overhead:** Traders spend 5-10 hours weekly on manual journaling and compliance monitoring instead of focusing on trading
- **Reactive Risk Management:** Existing solutions only report violations after they occur, when it's already too late to prevent account termination
- **Anxiety & Cognitive Load:** Constant vigilance required to track multiple prop firm rules creates stress and impairs trading decisions
- **Data Silos:** Trade history and performance insights trapped in disconnected systems prevent pattern recognition

---

## 3. Proposed Solution

### Core Value Proposition
TradeGuard acts as an automated compliance guardian and intelligent trading journal, preventing violations before they happen while building a comprehensive data foundation for trader improvement.

### Key Features

| Feature | Description | Value |
|---------|-------------|-------|
| **Real-Time Rule Engine** | EA intercepts orders pre-execution and blocks violations | Prevents 90%+ of accidental violations |
| **Automated Journal Sync** | Complete trade capture with screenshots, notes, market context | Saves 5-10 hours/week manual entry |
| **Prop Firm Rule Library** | Pre-configured rule sets for 10+ major firms (FTMO, The5ers, etc.) | One-click setup, reduces friction |
| **Risk Dashboard** | Visual real-time metrics vs. prop firm limits with color-coded alerts | Reduces trader anxiety |
| **Multi-Account Management** | Unified view across all trading accounts | Simplifies oversight for active traders |
| **Cloud Analytics** | Pattern detection, performance KPIs, behavioral insights | Data-driven improvement |

### Technical Architecture
- **MT5 EA Bridge:** MQL5-based terminal connector with WebSocket real-time streaming
- **Cloud Backend:** NoSQL time-series database for trade data with OAuth authentication
- **Web Dashboard:** React-based interface for configuration and analytics
- **Mobile Companion:** Push notifications and monitoring (post-MVP)

---

## 4. Target Users

### Primary Users
| Segment | Description | Pain Level | Willingness to Pay |
|---------|-------------|------------|-------------------|
| **Prop Firm Traders** | Traders with funded accounts or in evaluation phase | Very High | High |
| **EA Strategy Developers** | Developers deploying automated strategies across multiple accounts | High | Medium-High |
| **Multi-Account Traders** | Active traders managing 3+ accounts simultaneously | High | Medium |

### Secondary Users
| Segment | Description | Opportunity |
|---------|-------------|-------------|
| **Trading Educators/Coaches** | Mentors tracking student performance | B2B licensing |
| **Fund Managers** | Overseeing multiple trader accounts | Enterprise tier |
| **Prop Firms** | Seeking white-label compliance tools | B2B2C partnership |

### Market Size Context
- ~11 million active MT5 users globally
- Prop firm industry growing 200%+ annually
- 15+ major prop firms with varying rule sets

---

## 5. Success Metrics (KPIs)

| KPI | Target | Measurement |
|-----|--------|-------------|
| **Violation Prevention Rate** | >90% | % of potential violations blocked by rule engine |
| **User Time Savings** | 5+ hours/week | Self-reported + usage analytics |
| **Monthly Active Users (MAU)** | 1,000+ (Year 1) | Platform engagement metrics |
| **User Retention** | >70% at 3 months | Cohort retention analysis |
| **Net Promoter Score (NPS)** | >40 | Quarterly user surveys |

### Leading Indicators
- Rule configuration completion rate (activation metric)
- Daily sync frequency (engagement metric)
- Support ticket volume per user (quality metric)

---

## 6. MVP Scope

### Top 3 MVP Features (Priority Order)

#### 1. Real-Time Rule Engine with Pre-Trade Blocking ⭐ HIGHEST PRIORITY
**What:** EA intercepts trade execution and validates against configured prop firm rules before allowing orders to reach the broker

**Why:** Unique differentiator; converts "nice to have" into "cannot trade without"; solves #1 user pain point

**Scope:**
- MQL5 EA architecture for order interception
- Web UI for rule configuration
- Rule validation engine (drawdown limits, daily loss, position sizing)
- Alert/notification system for near-violations

**Timeline:** 6-8 weeks
**Resources:** 1 senior MQL5 developer, 1 backend, 1 frontend

---

#### 2. Automated Trade Journal Sync ⭐ HIGH PRIORITY
**What:** Complete trade history synchronization from MT5 to cloud with rich metadata

**Why:** Foundation for all analytics; establishes data moat; immediate time-saving value

**Scope:**
- Data schema for trade records + metadata
- Sync pipeline from MT5 EA to cloud
- Chart snapshot capture at entry/exit
- Basic journal view interface (list + detail)

**Timeline:** 4-5 weeks (parallel development)
**Resources:** 1 backend, 1 frontend, cloud infrastructure

---

#### 3. Prop Firm Rule Library ⭐ HIGH PRIORITY
**What:** Pre-configured rule sets for major prop firms with one-click import

**Why:** Massive friction reducer; makes platform accessible to non-technical traders; creates switching costs

**Scope:**
- Research & documentation for top 10 prop firms (FTMO, The5ers, MyForexFunds, etc.)
- Versioning system for rule changes
- Import/export functionality
- Community submission mechanism (basic)

**Timeline:** 3 weeks initial + ongoing updates
**Resources:** 1 researcher/analyst, 1 developer

---

### MVP Out of Scope (Post-MVP)
- AI-powered pattern recognition
- Mobile companion app
- Social/community features
- Marketplace for third-party add-ons
- Virtual AI trading coach
- White-label/B2B features

### Success Criteria for MVP
- [ ] Beta users report 90%+ violation prevention
- [ ] <100ms latency on trade validation
- [ ] Support for 5+ major prop firms
- [ ] 50+ beta signups from target segment
- [ ] Zero data loss or sync failures

---

## 7. Strategic Considerations

### Competitive Moats
1. **Rule Database:** Proprietary, maintained prop firm rule configurations
2. **Real-time Enforcement:** Technical capability competitors lack
3. **Data Network Effects:** More users → better pattern insights (anonymized)

### Key Risks
- MT5 API/broker dependency
- Prop firm rule changes breaking configurations
- Privacy concerns with cloud-stored trade data
- Regulatory uncertainty in some jurisdictions

### Next Steps
1. Technical proof-of-concept for MT5 order interception latency
2. User interviews with 10-15 prop firm traders
3. Partnership discussions with 2-3 prop firms
4. Pricing research across user segments

---

*Document generated from BMAD brainstorming session results*  
*Next Review: Upon completion of technical POC*
