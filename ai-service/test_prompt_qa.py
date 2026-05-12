import requests
import json
import time

BASE_URL = "http://127.0.0.1:5000"

with open("ai-service/demo_records.txt", "r") as f:
    records = [line.strip() for line in f.readlines() if line.strip()]

results = []

print("\n===== AI PROMPT QA TESTING =====\n")

for i, text in enumerate(records, start=1):

    print(f"\n[{i}] Testing:")
    print(text)

    try:

        start = time.time()

        response = requests.post(
            f"{BASE_URL}/categorise",
            json={
                "text": text
            }
        )

        end = time.time()

        response_time = round((end - start) * 1000, 2)

        data = response.json()

        print("Response:")
        print(json.dumps(data, indent=2))

        results.append({
            "input": text,
            "response": data,
            "response_time_ms": response_time
        })

    except Exception as e:

        print("ERROR:", e)

        results.append({
            "input": text,
            "error": str(e)
        })

print("\n===== TESTING COMPLETED =====")

with open("PROMPT_QA_RESULTS.json", "w") as f:
    json.dump(results, f, indent=2)

print("\nResults saved to PROMPT_QA_RESULTS.json")