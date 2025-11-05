# Sonya-API

A simple REST API built with **Flask**, containerized with **Docker**, and deployed via **Render**.

## 🚀 Project Overview
This project was created as part of the *Server-Side Software Technologies* course.  
It implements a minimal web service with one endpoint — `/healthcheck` — that returns the current date and service status in JSON format.

## 🧩 Tech Stack
- Python 3.13.5  
- Flask  
- Docker / Docker Compose  
- Render (deployment platform)

## 📦 Installation (Local)

1. **Create and activate a virtual environment**
   ```bash
   python3 -m venv env
   source env/bin/activate
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run locally**
   ```bash
   export FLASK_APP=app
   flask run --host 0.0.0.0 -p 8080
   ```

4. **Check**
   ```bash
   curl http://localhost:8080/healthcheck
   ```

## 🐳 Run with Docker

### Build and start manually
```bash
docker build -t sonya-api:latest .
docker run --rm -e PORT=8080 -p 8080:8080 sonya-api:latest
```

### Or using Docker Compose
```bash
docker compose up --build
```

## 🌐 Deployment
The app can be easily deployed to **Render**:
1. Push the project to GitHub.  
2. Create a new **Web Service** on [render.com](https://render.com).  
3. Connect the GitHub repo — Render will detect the Dockerfile automatically.  
4. Once deployed, visit:
   [https://sonya-api.onrender.com/healthcheck](https://sonya-api.onrender.com/healthcheck)

## ✅ Example Response
```json
{
  "status": "ok",
  "date": "2025-10-22T10:35:12Z"
}
```

---

> **Author:** Novakivska Sofia  
> **Group:** IO-35  

## 📚 Lab 2 — Expense Tracker API

### Endpoints
**Users**
- `POST /user` — create `{ "name": "Alice" }` → 201
- `GET /user/{id}` — get by id → 200/404
- `DELETE /user/{id}` — delete → 204/404
- `GET /users` — list → 200

**Categories**
- `POST /category` — create `{ "title": "Food" }` → 201
- `GET /category` — list → 200
- `DELETE /category?id={id}` — delete (or pass `{ "id": 1 }` in JSON) → 204/404

**Records**
- `POST /record` — create `{ "user_id": 1, "category_id": 1, "amount": 99.5, "created_at"?: ISO8601 }`  
  Validates that `user_id` and `category_id` exist. → 201/400
- `GET /record/{id}` — get by id → 200/404
- `DELETE /record/{id}` — delete → 204/404
- `GET /record?user_id=..&category_id=..` — filter by one or both. **Without params → 400**

### 🧪 Postman
Import the collection and environments:
- `Sonya-Lab2.postman_collection.json`
- `Sonya-Local.postman_environment.json`
- `Sonya-Production.postman_environment.json`

Then select the desired environment (`Local` or `Production`) and run the requests.

### 🔁 Postman Flow Testing

Below is an automated Flow scenario that verifies the end-to-end creation
of a User, Category, and Expense Record with dynamic ID references passed
between requests.

<p align="center">
  <img src="assets/flow-create-record.png" width="800"/>
</p>
<p align="center"><b>Figure 1.</b> Automated Flow for creating a complete expense record in Postman Flows</p>

<p align="center">
  <img src="assets/flow-success.png" width="800"/>
</p>
<p align="center"><b>Figure 2.</b> Successful execution results for the Flow scenario</p>


### ▶️ Run locally
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
export FLASK_APP=app
flask run
```

### 🐳 Docker
```bash
docker build -t sonya-api .
docker run -p 8080:8080 -e PORT=8080 sonya-api
```

### 🌐 Deployment
The app is deploy-ready for Render: the `Dockerfile` runs `flask --app app run -h 0.0.0.0 -p $PORT`.
