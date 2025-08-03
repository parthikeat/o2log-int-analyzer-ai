import os, requests, smtplib
from email.mime.text import MIMEText

def send_slack(message):
    webhook = os.getenv("SLACK_WEBHOOK")
    requests.post(webhook, json={"text": message})

def send_email(html_report):
    msg = MIMEText(html_report, 'html')
    msg['Subject'] = 'AI Log Analyzer Report'
    msg['From'] = os.getenv("SMTP_USER")
    msg['To'] = os.getenv("SMTP_USER")
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASSWORD"))
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
