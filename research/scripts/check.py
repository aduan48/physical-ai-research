"""Check that citations resolve and the CSV is valid. Run: python3 research/scripts/check.py"""
import csv, re, sys
from pathlib import Path

root = Path(__file__).resolve().parent.parent
errors = []

defined = set(re.findall(r"^\| (S\d+) \|", (root / "sources.md").read_text(), re.M))
for md in list((root / "industries").glob("*.md")) + [root / "README.md", root / "dig-deeper.md"]:
    for s in set(re.findall(r"\[(S\d+)\]", md.read_text())) - defined:
        errors.append(f"{md.name}: cites {s}, not in sources.md")

with open(root / "opportunities.csv", newline="") as f:
    rows = list(csv.DictReader(f))
ids = [r["id"] for r in rows]
if len(ids) != len(set(ids)):
    errors.append("duplicate ids in opportunities.csv")
for r in rows:
    for k in ("impact", "feasibility"):
        if r[k] not in "12345" or len(r[k]) != 1:
            errors.append(f"{r['id']}: {k}={r[k]!r} not 1-5")
    if not r["months_to_pilot"].isdigit():
        errors.append(f"{r['id']}: months_to_pilot not an integer")
    if not (root / r["file"]).exists():
        errors.append(f"{r['id']}: file {r['file']} missing")

print("\n".join(errors) or f"OK: {len(rows)} opportunities, {len(defined)} sources")
sys.exit(1 if errors else 0)
