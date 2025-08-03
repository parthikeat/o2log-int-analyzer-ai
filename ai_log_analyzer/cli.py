import argparse
from ai_log_analyzer.main import process_logs
from ai_log_analyzer.openobserve_fetcher import fetch_logs_by_id

def main():
    parser = argparse.ArgumentParser(description="AI Log Analyzer CLI")
    subparsers = parser.add_subparsers(dest="command")

    analyze_parser = subparsers.add_parser("analyze", help="Run full analysis pipeline")

    fetch_parser = subparsers.add_parser("fetch", help="Fetch logs by trace ID")
    fetch_parser.add_argument("--id", required=True, help="Trace ID")
    fetch_parser.add_argument("--start", required=True, help="Start time (ISO format)")
    fetch_parser.add_argument("--end", required=True, help="End time (ISO format)")

    args = parser.parse_args()

    if args.command == "analyze":
        process_logs()
    elif args.command == "fetch":
        logs = fetch_logs_by_id(args.id, args.start, args.end)
        print(f"Fetched {len(logs)} logs:")
        for log in logs:
            print(log)
