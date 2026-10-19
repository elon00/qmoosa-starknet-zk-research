"""Raven Recursive Self-Improvement & REA Governance Loop."""
def governed_rsi_cycle(metric_baseline: float, metric_candidate: float) -> dict:
    improved = metric_candidate > metric_baseline
    return {
        "baseline": metric_baseline,
        "candidate": metric_candidate,
        "status": "APPROVED" if improved else "REJECTED_REGRESSION",
        "delta": round(metric_candidate - metric_baseline, 4)
    }
