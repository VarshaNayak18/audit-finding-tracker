from flask import Blueprint, request, jsonify

bp = Blueprint("webhook_receiver", __name__)


@bp.route("/webhook-receiver", methods=["POST"])
def webhook_receiver():

    data = request.get_json()

    print("\nWEBHOOK RECEIVED")
    print(data)

    return jsonify({
        "message": "Webhook received successfully"
    })