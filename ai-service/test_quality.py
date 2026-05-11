import requests
import json

TEST_INPUTS = [
    "SQL injection vulnerability in login module",
    "Weak password policy enforced",
    "Missing API authentication",
    "Cross-site scripting vulnerability detected",
    "Hardcoded credentials found in source code",
    "Sensitive customer data stored unencrypted",
    "Improper access control in admin panel",
    "Lack of audit logging for transactions",
    "Insecure file upload validation",
    "Data leakage through application logs"
]

URL = "http://127.0.0.1:5000/categorise"

results = []

total_score = 0

print("\n===== AI QUALITY REVIEW =====\n")

for i, text in enumerate(TEST_INPUTS, start=1):

    payload = {
        "text": text
    }

    try:
        response = requests.post(URL, json=payload)

        print("Status Code:", response.status_code)
        print("Raw Response:", response.text)
        
        try:
            data = response.json()
        except Exception as e:
            print("JSON Parse Error:", str(e))
            continue

        category = data.get("data", {}).get("category", "Unknown")
        confidence = data.get("data", {}).get("confidence", 0)

        # Simple scoring logic
        if confidence >= 0.9:
            score = 5
        elif confidence >= 0.8:
            score = 4
        elif confidence >= 0.7:
            score = 3
        elif confidence >= 0.5:
            score = 2
        else:
            score = 1

        total_score += score

        result = {
            "input": text,
            "category": category,
            "confidence": confidence,
            "score": score
        }

        results.append(result)

        print(f"{i}. {text}")
        print(f"   Category  : {category}")
        print(f"   Confidence: {confidence}")
        print(f"   Score     : {score}/5\n")

    except Exception as e:
        print(f"Error testing input: {text}")
        print(str(e))

average_score = total_score / len(TEST_INPUTS)

print("===== FINAL REPORT =====")
print(f"Average Score: {round(average_score, 2)}/5")

# Save report
with open("ai-service/AI_EVALUATION.md", "w") as f:

    f.write("# AI Quality Review — Day 10\n\n")

    f.write("| Input | Category | Confidence | Score |\n")
    f.write("|------|------|------|------|\n")

    for r in results:
        f.write(
            f"| {r['input']} | {r['category']} | {r['confidence']} | {r['score']}/5 |\n"
        )

    f.write(f"\n## Average Score\n\n{round(average_score, 2)}/5\n")

print("\nEvaluation report saved to AI_EVALUATION.md")