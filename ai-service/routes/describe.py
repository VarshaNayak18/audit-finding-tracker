from flask import Blueprint, g, jsonify

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = g.sanitized_data

    text = data.get("text")

    return jsonify({
        "message": "Processed successfully",
        "clean_text": text
    })
