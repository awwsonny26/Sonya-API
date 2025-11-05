from flask import jsonify, request
from datetime import datetime, timezone
from . import app
from typing import Any, Dict

users = {}
categories = {}
records = {}

_seq = {"user": 1, "category": 1, "record": 1}


def _next(kind: str) -> int:
    _seq[kind] += 1
    return _seq[kind] - 1


def _iso_now():
    return datetime.now(timezone.utc).isoformat()


def _parse_int_field(data: Dict[str, Any], field: str) -> int:
    if field not in data:
        raise ValueError(f"Field '{field}' is required.")
    v = data[field]
    if isinstance(v, bool):
        raise ValueError(f"Field '{field}' must be an integer.")
    if isinstance(v, int):
        return v
    if isinstance(v, str):
        s = v.strip().replace("_", "")
        if s.lstrip("+-").isdigit():
            return int(s)
    raise ValueError(f"Field '{field}' must be an integer.")


def _parse_float_field(data: Dict[str, Any], field: str) -> float:
    if field not in data:
        raise ValueError(f"Field '{field}' is required.")
    v = data[field]
    try:
        return float(v)
    except Exception:
        raise ValueError(f"Field '{field}' must be a number.")


def problem(status: int, title: str, detail: str = ""):
    payload = {"status": status, "title": title}
    if detail:
        payload["detail"] = detail
    return jsonify(payload), status


@app.get("/healthcheck")
def healthcheck():
    return jsonify({"status": "ok", "date": _iso_now()}), 200
