"""Small support application. Python standard library only; no network calls."""
import argparse
import json
from pathlib import Path
from triage import prioritize

def build_report(tickets):
    report = []
    for ticket in tickets:
        try:
            report.append(prioritize(ticket))
        except ValueError as exc:
            report.append({"id": ticket.get("id", "unknown"), "error": str(exc)})
    return report

def main():
    parser = argparse.ArgumentParser(description="Review proposed ticket priorities")
    parser.add_argument("--input", default=str(Path(__file__).parent / "data/tickets.json"))
    args = parser.parse_args()
    tickets = json.loads(Path(args.input).read_text(encoding="utf-8"))
    print(json.dumps(build_report(tickets), indent=2))

if __name__ == "__main__":
    main()
