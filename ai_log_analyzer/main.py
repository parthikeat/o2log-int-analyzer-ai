import json
from ai_log_analyzer.summarizer import summarize_logs
from ai_log_analyzer.sop_checker import check_compliance
from ai_log_analyzer.notifications import send_slack, send_email

def process_logs():
    with open("logs.json") as f:
        logs = json.load(f)
    chunks = [logs[i:i+50] for i in range(0, len(logs), 50)]
    summary = summarize_logs(chunks)
    compliance = check_compliance(summary, "SOP_Document.xlsx")
    html_report = f"<h1>Summary</h1><p>{summary}</p><h2>Compliance</h2><ul>{''.join(f'<li>{c}</li>' for c in compliance)}</ul>"
    send_email(html_report)
    send_slack("Log analysis completed!")
