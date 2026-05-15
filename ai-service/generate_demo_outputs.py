import json
import requests

BASE_URL = "http://127.0.0.1:5000"

with open("ai-service/demo_outputs/demo_records.json", "r") as f:
    records = json.load(f)

results = []

print("\n===== GENERATING DEMO OUTPUTS =====\n")

for record in records:

    response = requests.post(
        f"{BASE_URL}/categorise",
        json=record
    )

    try:
        data = response.json()
    except:
        data = {
            "error": "Invalid response"
        }

    results.append({
        "input": record,
        "output": data
    })

    print(f"Processed: {record['text']}")

with open(
    "ai-service/demo_outputs/demo_results.json",
    "w"
) as f:

    json.dump(results, f, indent=4)

print("\nDemo outputs saved successfully.")