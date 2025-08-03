import pandas as pd

def check_compliance(summary_text, sop_path):
    df = pd.read_excel(sop_path)
    non_compliance = []
    for _, row in df.iterrows():
        if str(row['Expected']).lower() not in summary_text.lower():
            non_compliance.append(f"Missing: {row['Expected']}")
    return non_compliance
