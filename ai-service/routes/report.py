from flask import Blueprint, g, jsonify
from config import limiter

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
@limiter.limit("10 per minute")
def generate_report():
    data = g.sanitized_data

    return jsonify({
        "message": "Report generated",
        "data": data
    })