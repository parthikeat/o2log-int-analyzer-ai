import requests, os

def fetch_logs_by_id(trace_id, start_time, end_time):
    url = f"{os.getenv('OPENOBSERVE_URL')}/query"
    headers = {"Authorization": f"Bearer {os.getenv('OPENOBSERVE_TOKEN')}"}
    query = {
        "sql": f"SELECT * FROM logs WHERE trace_id = '{trace_id}' AND timestamp BETWEEN '{start_time}' AND '{end_time}'"
    }
    response = requests.post(url, headers=headers, json=query)
    response.raise_for_status()
    return response.json().get("hits", [])
