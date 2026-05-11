from flask import Flask

from routes.categorise import bp as categorise_bp
from routes.query import bp as query_bp
from routes.health import bp as health_bp

from routes.async_report import bp as async_report_bp
from routes.job_status import bp as job_status_bp

from routes.webhook_receiver import bp as webhook_receiver_bp

app = Flask(__name__)

app.register_blueprint(categorise_bp)
app.register_blueprint(query_bp)
app.register_blueprint(health_bp)

app.register_blueprint(async_report_bp)
app.register_blueprint(job_status_bp)

app.register_blueprint(webhook_receiver_bp)

@app.route("/")
def home():
    return {"message": "AI Service Running"}

if __name__ == "__main__":
    app.run(port=5000, debug=True)