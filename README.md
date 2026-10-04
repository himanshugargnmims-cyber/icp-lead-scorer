# 🎯 ICP Lead Scorer

<div align="center">

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)](https://python.org)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/himanshugargnmims-cyber/icp-lead-scorer)
[![Follow on GitHub](https://img.shields.io/github/followers/himanshugargnmims-cyber?label=Follow&style=social)](https://github.com/himanshugargnmims-cyber)

**4-Pillar B2B Account Scoring, Firmographic & Technographic Enrichment, and Intent Propensity Engine.**

</div>

---

## 🚀 The 4-Pillar Scoring Model

1. **Firmographic Fit (25 pts)**: Employee band, industry taxonomy, revenue run-rate.
2. **Technographic Alignment (25 pts)**: Stack compatibility (Salesforce, Snowflake, Stripe, HubSpot, AWS).
3. **Growth & Intent Signals (25 pts)**: Recent capital rounds (Series B+), headcount growth velocity (>20% YoY).
4. **Strategic Territory Fit (25 pts)**: Global footprint, enterprise parent account relationship.

---

## 💻 Quick Start

### 1. Installation
```bash
git clone https://github.com/himanshugargnmims-cyber/icp-lead-scorer.git
cd icp-lead-scorer
pip install -r requirements.txt
```

### 2. CLI Usage
```bash
python icp_scorer/cli.py --name "Stripe" --employees 8000 --industry "FinTech" --stack "Salesforce,Snowflake,AWS" --funding "Public"
```

### 3. Python SDK
```python
from icp_scorer import ICPScoringEngine

engine = ICPScoringEngine()
res = engine.score_account({
    "name": "CloudScale",
    "employee_count": 1200,
    "industry": "B2B SaaS",
    "tech_stack": ["Salesforce", "Snowflake", "Stripe"],
    "recent_funding_series": "Series C",
    "hiring_growth_pct": 25,
    "has_global_presence": True
})
print("Total ICP Score:", res["total_score"])
print("Routing Tier:", res["tier"])
```

## 📄 License
MIT License. See [`LICENSE`](LICENSE).
