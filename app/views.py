from flask import jsonify
from datetime import datetime, timezone
from . import app


@app.get("/healthcheck")
def healthcheck():
    return (
        jsonify({"status": "ok", "date": datetime.now(timezone.utc).isoformat()}),
        200,
    )
