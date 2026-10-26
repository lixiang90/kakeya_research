"""Read-only recovery entry point; concise by default, exact archive with --full."""
import argparse
from collections import Counter
import json
from pathlib import Path
import re
import sys


def main():
    sys.stdout.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--full", action="store_true", help="Print complete historical files and registry")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    for name in ("GOAL.md", "STATE.md", "ROADMAP.md", "results/registry.json"):
        path = root / name
        print(f"\n===== {name} =====")
        if not path.exists():
            print("MISSING: restore before research")
            continue
        content = path.read_text(encoding="utf-8")
        if args.full or name in ("GOAL.md", "STATE.md"):
            print(content)
        elif name == "ROADMAP.md":
            # The route table precedes chronological entries; preserve it in full.
            print(content.split("\nDIR003", 1)[0])
            print("Historical entries remain in ROADMAP.md; use targeted rg or --full.")
        else:
            data = json.loads(content)
            items = data.get("items", [])
            summary = {key: data.get(key) for key in (
                "updated_on", "latest_round", "current_goal_tool_status", "next_main_spec",
                "active_research_goal", "latest_research_restart") if key in data}
            summary["item_count"] = len(items)
            summary["statuses"] = dict(Counter(item.get("status", "unspecified") for item in items))
            summary["baseline_result"] = next(({
                key: item[key] for key in ("id", "status", "file", "proof", "depends_on") if key in item
            } for item in items if item.get("id") == "DIM-001"), None)
            print(json.dumps(summary, ensure_ascii=False, indent=2))
            print("Full item details and failed-equivalence records remain in registry.json.")
    rounds = sorted((root / "research/rounds").glob("R*.md"), reverse=True)
    # Include editorial/restart rounds as well as the old Rxxxx.md convention.
    latest = next((p for p in rounds if re.fullmatch(r"R\d{4}(?:_[A-Za-z0-9_]+)?\.md", p.name)
                   and not any(word in p.stem for word in ("spec", "TEMPLATE"))), None)
    if latest:
        print(f"\n===== latest round: {latest.name} =====")
        print(latest.read_text(encoding="utf-8"))
    print("\nRead the current main spec and relevant original proofs before mathematics; this summary is navigation, not a proof.")


if __name__ == "__main__":
    main()
