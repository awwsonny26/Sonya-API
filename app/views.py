from flask import jsonify
from datetime import datetime
from . import app

@app.get("/healthcheck")
def healthcheck():
    return jsonify({
        "status": "ok",
        "date": datetime.utcnow().isoformat() + "Z"
    }), 200
