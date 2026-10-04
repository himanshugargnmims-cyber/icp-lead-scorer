#!/usr/bin/env python3
"""
CLI entry point for ICP Lead Scorer
"""

import argparse
from icp_scorer.engine import ICPScoringEngine


def main():
    parser = argparse.ArgumentParser(description="ICP Lead Scorer — 4-Pillar Account Propensity Engine")
    parser.add_argument("--name", type=str, default="Stripe", help="Account name")
    parser.add_argument("--employees", type=int, default=8000, help="Employee headcount")
    parser.add_argument("--industry", type=str, default="FinTech SaaS", help="Industry vertical")
    parser.add_argument("--stack", type=str, default="Salesforce,Snowflake,AWS", help="Comma-separated tech stack")
    parser.add_argument("--funding", type=str, default="Public", help="Recent funding round")
    parser.add_argument("--growth", type=int, default=25, help="YoY hiring headcount growth %")

    args = parser.parse_args()

    engine = ICPScoringEngine()
    account = {
        "name": args.name,
        "employee_count": args.employees,
        "industry": args.industry,
        "tech_stack": [s.strip() for s in args.stack.split(",")],
        "recent_funding_series": args.funding,
        "hiring_growth_pct": args.growth,
        "has_global_presence": True,
        "is_enterprise_target": True
    }
    res = engine.score_account(account)

    print("\n" + "=" * 72)
    print("                 B2B ACCOUNT ICP PROPENSITY REPORT")
    print("=" * 72)
    print(f"  Target Account:            {res['account_name']}")
    print(f"  Total ICP Score:           {res['total_score']:.1f} / 100.0")
    print(f"  Account Routing Tier:      {res['tier']}")
    print("-" * 72)
    print("  4-Pillar Score Breakdown:")
    print(f"    • Firmographic Fit:      {res['pillar_breakdown']['firmographic_score']} / 25.0")
    print(f"    • Technographic Match:   {res['pillar_breakdown']['technographic_score']} / 25.0 ({', '.join(res['technographic_matches'])})")
    print(f"    • Growth & Intent:       {res['pillar_breakdown']['growth_intent_score']} / 25.0")
    print(f"    • Strategic Alignment:   {res['pillar_breakdown']['strategic_fit_score']} / 25.0")
    print("=" * 72 + "\n")


if __name__ == "__main__":
    main()
