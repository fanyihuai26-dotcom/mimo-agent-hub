"""
MiMo Agent Hub - Reviewer Agent

Validates executor outputs and provides feedback for iterative refinement.
Ensures quality through multi-criteria evaluation.
"""

from __future__ import annotations

import os
from typing import Any

# MiMo API configuration
MIMO_API_KEY = os.getenv("MIMO_API_KEY", "")
MIMO_API_BASE = os.getenv("MIMO_API_BASE", "https://api.mimo.com/v1")


def review_step(step_result: dict[str, Any]) -> dict[str, Any]:
    """
    Review the output of a single execution step.

    Args:
        step_result: The result dict from the executor.

    Returns:
        Review verdict with quality score and optional feedback.
    """
    output = step_result.get("output", "")

    # TODO: Replace with actual MiMo API call for LLM-based review
    # Current: heuristic-based review for MVP
    quality_score = _evaluate_quality(output)
    passed = quality_score >= 0.7

    review = {
        "step_id": step_result.get("step_id"),
        "quality_score": quality_score,
        "passed": passed,
        "feedback": None if passed else "Output needs more detail and specificity.",
    }

    return review


def review_plan_results(
    plan_results: list[dict[str, Any]],
) -> dict[str, Any]:
    """
    Review all execution results from a completed plan.

    Args:
        plan_results: List of step result dicts from the executor.

    Returns:
        Aggregate review with overall score and per-step feedback.
    """
    reviews = [review_step(r) for r in plan_results]
    scores = [r["quality_score"] for r in reviews]
    avg_score = sum(scores) / len(scores) if scores else 0.0

    failed_steps = [r for r in reviews if not r["passed"]]

    return {
        "overall_score": avg_score,
        "all_passed": len(failed_steps) == 0,
        "total_steps": len(reviews),
        "passed_steps": len(reviews) - len(failed_steps),
        "failed_steps": len(failed_steps),
        "reviews": reviews,
        "needs_revision": len(failed_steps) > 0,
    }


def _evaluate_quality(output: str) -> float:
    """
    Heuristic quality evaluation based on output characteristics.
    Returns a score between 0.0 and 1.0.
    """
    if not output:
        return 0.0

    score = 0.5  # base score

    # Reward longer, more detailed outputs
    if len(output) > 20:
        score += 0.1
    if len(output) > 50:
        score += 0.1

    # Reward structured output (brackets, labels)
    if "[" in output and "]" in output:
        score += 0.1

    return min(score, 1.0)
