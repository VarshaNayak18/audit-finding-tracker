import re
from flask import request, jsonify, g

# Expanded prompt injection patterns (case-insensitive)
PROMPT_INJECTION_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"act\s+as\s+system",
    r"bypass\s+restrictions",
    r"you\s+are\s+now",
    r"forget\s+all\s+rules",
    r"reveal\s+.*prompt",
    r"system\s+prompt",
]

HTML_TAG_PATTERN = re.compile(r"<.*?>")
MAX_INPUT_LENGTH = 2000
ALLOWED_PATTERN = re.compile(r"^[a-zA-Z0-9\s.,!?@#()\-_:;/]*$")

def is_safe_input(text):
    return bool(ALLOWED_PATTERN.match(text))

def sanitize_text(text: str) -> str:
    text = re.sub(HTML_TAG_PATTERN, "", text)
    return text.strip()


def contains_prompt_injection(text: str) -> bool:
    text_lower = text.lower()
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, text_lower):
            return True
    return False


def sanitize_all_fields(data):
    if not data:
        return False, "Empty request body"

    if not isinstance(data, dict):
        return False, "Invalid JSON format"

    for key, value in data.items():
        if isinstance(value, str):

            if len(value.strip()) == 0:
                return False, f"{key} cannot be empty"

            if len(value) > MAX_INPUT_LENGTH:
                return False, f"{key} exceeds max length"

            if contains_prompt_injection(value):
                print(f"[SECURITY] Prompt injection attempt in field: {key}")
                return False, "Prompt injection detected"

            if not is_safe_input(value):
                print(f"[SECURITY] Unsafe input detected in field: {key}")
                return False, "Unsafe input detected"

            data[key] = sanitize_text(value)

    return True, data


def sanitize_request():
    if request.method in ["POST", "PUT"]:
        data = request.get_json(silent=True)

        is_valid, result = sanitize_all_fields(data)

        if not is_valid:
            return jsonify({"error": result}), 400

        # Store sanitized data safely
        g.sanitized_data = result
        print("[INFO] Sanitized Request:", result)