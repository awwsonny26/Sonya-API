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


@app.post("/user")
def create_user():
    data = request.get_json(silent=True) or {}
    name = data.get("name")
    if not name:
        return problem(400, "Bad Request", "Field 'name' is required.")
    uid = _next("user")
    users[uid] = {"id": uid, "name": name}
    return jsonify(users[uid]), 201


@app.get("/user/<int:user_id>")
def get_user(user_id: int):
    u = users.get(user_id)
    if not u:
        return problem(404, "Not Found", f"User {user_id} not found.")
    return jsonify(u), 200


@app.delete("/user/<int:user_id>")
def delete_user(user_id: int):
    if user_id not in users:
        return problem(404, "Not Found", f"User {user_id} not found.")
    to_delete = [rid for rid, r in records.items() if r["user_id"] == user_id]
    for rid in to_delete:
        records.pop(rid, None)
    users.pop(user_id, None)
    return ("", 204)


@app.get("/users")
def list_users():
    return jsonify(list(users.values())), 200


@app.get("/category")
def list_categories():
    return jsonify(list(categories.values())), 200


@app.post("/category")
def create_category():
    data = request.get_json(silent=True) or {}
    title = data.get("title")
    if not title:
        return problem(400, "Bad Request", "Field 'title' is required.")
    cid = _next("category")
    categories[cid] = {"id": cid, "title": title}
    return jsonify(categories[cid]), 201


@app.delete("/category")
def delete_category():
    cid = request.args.get("id", type=int)
    if cid is None:
        body = request.get_json(silent=True) or {}
        cid = body.get("id")
        try:
            cid = int(cid) if cid is not None else None
        except Exception:
            cid = None
    if cid is None:
        return problem(
            400, "Bad Request", "Query param 'id' (or JSON field 'id') is required."
        )
    if cid not in categories:
        return problem(404, "Not Found", f"Category {cid} not found.")
    to_delete = [rid for rid, r in records.items() if r["category_id"] == cid]
    for rid in to_delete:
        records.pop(rid, None)
    categories.pop(cid, None)
    return ("", 204)


@app.post("/record")
def create_record():
    data: Dict[str, Any] = request.get_json(silent=True) or {}
    try:
        user_id = _parse_int_field(data, "user_id")
        category_id = _parse_int_field(data, "category_id")
        amount = _parse_float_field(data, "amount")
    except ValueError as e:
        return problem(400, "Bad Request", str(e))

    if user_id not in users:
        return problem(400, "Bad Request", f"user_id {user_id} does not exist.")
    if category_id not in categories:
        return problem(400, "Bad Request", f"category_id {category_id} does not exist.")

    created_at = str(data.get("created_at") or _iso_now())
    rid = _next("record")
    record = {
        "id": rid,
        "user_id": user_id,
        "category_id": category_id,
        "amount": amount,
        "created_at": created_at,
    }
    records[rid] = record
    return jsonify(record), 201


@app.get("/record/<int:record_id>")
def get_record(record_id: int):
    rec = records.get(record_id)
    if not rec:
        return problem(404, "Not Found", f"Record {record_id} not found.")
    return jsonify(rec), 200


@app.delete("/record/<int:record_id>")
def delete_record(record_id: int):
    if record_id not in records:
        return problem(404, "Not Found", f"Record {record_id} not found.")
    records.pop(record_id, None)
    return ("", 204)


@app.get("/record")
def list_records():
    user_id = request.args.get("user_id", type=int)
    category_id = request.args.get("category_id", type=int)
    if user_id is None and category_id is None:
        return problem(
            400,
            "Bad Request",
            "Provide at least one filter: user_id and/or category_id.",
        )
    items = list(records.values())
    if user_id is not None:
        items = [r for r in items if r["user_id"] == user_id]
    if category_id is not None:
        items = [r for r in items if r["category_id"] == category_id]
    return jsonify(items), 200
