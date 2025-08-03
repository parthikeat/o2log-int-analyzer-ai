import openai, os

def summarize_logs(log_chunks):
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    combined_summary = []
    for chunk in log_chunks:
        response = client.responses.create(
            model="gpt-4.1",
            input=f"Summarize and rank top errors:\n{chunk}"
        )
        combined_summary.append(response.output_text)
    return "\n".join(combined_summary)
