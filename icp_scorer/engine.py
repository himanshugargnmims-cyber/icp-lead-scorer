"""
4-Pillar B2B SaaS ICP & Lead Propensity Scoring Engine
"""

from typing import Dict, List, Any


class ICPScoringEngine:
    """
    Evaluates accounts and inbound leads across 4 pillars:
    1. Firmographic Fit (25 pts)
    2. Technographic Fit (25 pts)
    3. Growth & Intent Signals (25 pts)
    4. Strategic Alignment (25 pts)
    """

    TARGET_STACK = {"salesforce", "snowflake", "stripe", "hubspot", "segment", "aws", "databricks"}

    def score_account(self, account: Dict[str, Any]) -> Dict[str, Any]:
        firmo_score = 0.0
        techno_score = 0.0
        intent_score = 0.0
        strat_score = 0.0

        # 1. Firmographics
        emp_count = account.get("employee_count", 0)
        if 200 <= emp_count <= 5000:
            firmo_score += 15.0
        elif emp_count > 5000:
            firmo_score += 10.0
        else:
            firmo_score += 5.0

        industry = account.get("industry", "").lower()
        if any(kw in industry for kw in ["saas", "fintech", "cloud", "software", "ai"]):
            firmo_score += 10.0

        # 2. Technographics
        stack = [t.lower() for t in account.get("tech_stack", [])]
        matched_stack = [t for t in stack if t in self.TARGET_STACK]
        techno_score = min(25.0, len(matched_stack) * 7.5)

        # 3. Growth & Intent
        funding = account.get("recent_funding_series", "").lower()
        if any(f in funding for f in ["series b", "series c", "series d", "growth", "public"]):
            intent_score += 15.0
        elif "series a" in funding:
            intent_score += 10.0

        hiring_growth = account.get("hiring_growth_pct", 0)
        if hiring_growth >= 20:
            intent_score += 10.0
        elif hiring_growth >= 10:
            intent_score += 5.0

        # 4. Strategic Alignment
        if account.get("has_global_presence", False):
            strat_score += 12.5
        if account.get("is_enterprise_target", True):
            strat_score += 12.5

        total_score = firmo_score + techno_score + intent_score + strat_score

        if total_score >= 80.0:
            tier = "Tier 1: Strategic Enterprise VIP (Dedicated Named AE)"
        elif total_score >= 60.0:
            tier = "Tier 2: High-Yield Mid-Market (Commercial AE)"
        else:
            tier = "Tier 3: Product-Led / Self-Serve Nurture"

        return {
            "account_name": account.get("name", "Unknown Account"),
            "total_score": round(total_score, 1),
            "tier": tier,
            "pillar_breakdown": {
                "firmographic_score": round(firmo_score, 1),
                "technographic_score": round(techno_score, 1),
                "growth_intent_score": round(intent_score, 1),
                "strategic_fit_score": round(strat_score, 1)
            },
            "technographic_matches": matched_stack
        }
