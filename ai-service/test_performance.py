import requests
import time
import statistics

BASE_URL = "http://127.0.0.1:5000"

records = [
    "SQL injection vulnerability in login module",
    "Weak password policy detected",
    "Missing API authentication",
    "Sensitive customer data stored unencrypted",
    "Improper access control in admin dashboard"
]

response_times = []

print("\n===== PERFORMANCE TEST =====\n")

for i, text in enumerate(records, start=1):

    print(f"Test {i}")

    start = time.time()

    response = requests.post(
        f"{BASE_URL}/categorise",
        json={
            "text": text
        }
    )

    end = time.time()

    response_time = round((end - start) * 1000, 2)

    response_times.append(response_time)

    print(f"Input: {text}")
    print(f"Status Code: {response.status_code}")
    print(f"Response Time: {response_time} ms")
    print()

avg_time = round(statistics.mean(response_times), 2)

print("===== FINAL REPORT =====")
print(f"Average Response Time: {avg_time} ms")
print(f"Fastest Response: {min(response_times)} ms")
print(f"Slowest Response: {max(response_times)} ms")