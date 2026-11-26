import csv
from pathlib import Path
ROOT = Path(__file__).resolve().parent
def assess(row, controls):
    failed = [c for c in controls if int(row[c["control"]]) == 1]
    score = sum(int(c["weight"]) for c in failed)
    tier = "High" if score >= 40 or int(row["regulatory"]) else "Moderate" if score >= 20 else "Low"
    return dict(row, score=score, tier=tier, exceptions=len(failed), actions="; ".join(c["corrective_action"] for c in failed))
def main():
    with (ROOT / "data/control_matrix.csv").open() as f:
        controls = list(csv.DictReader(f))
    with (ROOT / "data/suppliers.csv").open() as f:
        results = [assess(r, controls) for r in csv.DictReader(f)]
    out = ROOT / "reports/risk_register.csv"
    out.parent.mkdir(exist_ok=True)
    with out.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=results[0].keys())
        writer.writeheader()
        writer.writerows(results)
    print({t: sum(r["tier"] == t for r in results) for t in ("High", "Moderate", "Low")})
if __name__ == "__main__":
    main()
