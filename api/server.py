"""
MiMo Agent Hub - FastAPI Server

Main API server for the multi-agent automation platform.
Provides REST endpoints for task submission, plan inspection, and execution.
"""

from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from agents.executor import execute_plan, execute_step
from agents.planner import plan_task, replan
from agents.reviewer import review_plan_results, review_step

app = FastAPI(
    title="MiMo Agent Hub",
    description="Multi-agent AI automation platform powered by MiMo",
    version="0.1.0",
)


# ── Request / Response Models ──────────────────────────────────────────


class TaskRequest(BaseModel):
    task: str
    context: Optional[Dict[str, Any]] = None


class ReplanRequest(BaseModel):
    plan: Dict[str, Any]
    feedback: str


class StepResult(BaseModel):
    step_id: Optional[int] = None
    action: str
    output: str
    status: str = "completed"


# ── Endpoints ──────────────────────────────────────────────────────────


@app.get("/")
def root() -> Dict[str, str]:
    return {
        "message": "MiMo Agent Hub running",
        "version": "0.1.0",
        "docs": "/docs",
    }


@app.post("/plan")
def create_plan(req: TaskRequest) -> Dict[str, Any]:
    """Create an execution plan for a given task."""
    plan = plan_task(req.task, req.context)
    return plan


@app.post("/execute")
def execute_full_plan(req: TaskRequest) -> Dict[str, Any]:
    """
    End-to-end: plan → execute → review.

    This is the primary endpoint for autonomous task execution.
    Consumes the most MiMo API tokens due to multi-agent orchestration.
    """
    # 1. Plan
    plan = plan_task(req.task, req.context)

    # 2. Execute all steps
    execution_results = execute_plan(plan)

    # 3. Review results
    review = review_plan_results(execution_results)

    return {
        "task": req.task,
        "plan": plan,
        "results": execution_results,
        "review": review,
    }


@app.post("/execute/step")
def execute_single_step(step: Dict[str, Any]) -> Dict[str, Any]:
    """Execute a single step and review it individually."""
    result = execute_step(step)
    review = review_step(result)
    return {"result": result, "review": review}


@app.post("/replan")
def replan_task(req: ReplanRequest) -> Dict[str, Any]:
    """Adjust an existing plan based on reviewer feedback."""
    updated_plan = replan(req.plan, req.feedback)
    return updated_plan


@app.get("/health")
def health_check() -> Dict[str, str]:
    return {"status": "healthy"}


# ── Entry Point ────────────────────────────────────────────────────────

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
