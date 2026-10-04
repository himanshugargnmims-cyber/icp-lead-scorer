from icp_scorer.engine import ICPScoringEngine


def test_icp_score_calculation():
    engine = ICPScoringEngine()
    account = {
        "name": "CloudScale",
        "employee_count": 1200,
        "industry": "B2B SaaS",
        "tech_stack": ["Salesforce", "Snowflake", "Stripe"],
        "recent_funding_series": "Series C",
        "hiring_growth_pct": 30,
        "has_global_presence": True,
        "is_enterprise_target": True
    }
    res = engine.score_account(account)
    assert res["total_score"] >= 80.0
    assert "Tier 1" in res["tier"]
    assert len(res["technographic_matches"]) == 3
