"""
MiMo Agent Hub - Demo Task

Example script demonstrating the full agent workflow:
1. Submit a task via the API
2. View the generated plan, execution, and review results
"""

import json

import requests

API_BASE = "http://localhost:8000"


def run_demo():
    """Run a demo task through the MiMo Agent Hub API."""
    task = "Build a simple todo application with FastAPI backend and React frontend"

    print(f"🚀 Submitting task: {task}\n")

    response = requests.post(
        f"{API_BASE}/execute",
        json={"task": task},
        timeout=60,
    )

    if response.status_code != 200:
        print(f"❌ Error: {response.status_code}")
        print(response.text)
        return

    result = response.json()

    # Print plan
    print("📋 Plan:")
    for step in result["plan"]["steps"]:
        print(f"  Step {step['id']}: [{step['action']}] {step['description']}")

    # Print execution results
    print("\n⚡ Execution Results:")
    for r in result["results"]:
        print(f"  Step {r['step_id']}: {r['output']}")

    # Print review
    review = result["review"]
    print(f"\n🔍 Review:")
    print(f"  Overall Score: {review['overall_score']:.2f}")
    print(f"  All Passed: {review['all_passed']}")
    print(f"  Steps Passed: {review['passed_steps']}/{review['total_steps']}")

    if review["needs_revision"]:
        print("\n🔄 Needs revision - would trigger replan in production")


if __name__ == "__main__":
    run_demo()
