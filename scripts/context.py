"""Read-only compact handoff; run at the start of a resumed research turn."""
from pathlib import Path
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
root = Path(__file__).resolve().parents[1]
for name in ("GOAL.md", "STATE.md", "ROADMAP.md", "results/registry.json"):
    path = root / name
    print(f"\n===== {name} =====")
    print(path.read_text(encoding="utf-8") if path.exists() else "MISSING: restore before research")
rounds = sorted(p for p in (root / "research/rounds").glob("R*.md")
                if re.fullmatch(r"R\d{4}\.md", p.name))
if rounds:
    print(f"\n===== latest round: {rounds[-1].name} =====")
    print(rounds[-1].read_text(encoding="utf-8"))
