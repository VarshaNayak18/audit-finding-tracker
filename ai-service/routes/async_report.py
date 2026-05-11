from flask import Blueprint, request, jsonify
from threading import Thread
from services.job_store import jobs
from services.groq_client import GroqClient
import uuid
import time

bp = Blueprint("async_report", __name__)

client = GroqClient()


def generate_report_job(job_id, text):

    try:

        jobs[job_id]["status"] = "processing"

        prompt = f"""
        Generate a professional audit report for:

        {text}
        """

        result = client.generate(prompt)

        time.sleep(5)

        jobs[job_id]["status"] = "completed"

        jobs[job_id]["result"] = result["output"]

    except Exception as e:

        jobs[job_id]["status"] = "failed"

        jobs[job_id]["error"] = str(e)


@bp.route("/generate-report", methods=["POST"])
def generate_report():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Missing text field"
        }), 400

    text = data["text"]

    job_id = str(uuid.uuid4())

    jobs[job_id] = {
        "status": "queued",
        "result": None
    }

    thread = Thread(
        target=generate_report_job,
        args=(job_id, text)
    )

    thread.start()

    return jsonify({
        "job_id": job_id,
        "status": "queued"
    })