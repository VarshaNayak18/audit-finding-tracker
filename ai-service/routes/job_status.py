from flask import Blueprint, jsonify
from services.job_store import jobs

bp = Blueprint("job_status", __name__)


@bp.route("/job/<job_id>", methods=["GET"])
def get_job(job_id):

    job = jobs.get(job_id)

    if not job:
        return jsonify({
            "error": "Job not found"
        }), 404

    return jsonify(job)