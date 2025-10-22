# Sonya-API

A simple REST API built with **Flask**, containerized with **Docker**, and deployed via **Render**.

## 🚀 Project Overview
This project was created as part of the *Server-Side Software Technologies* course.  
It implements a minimal web service with one endpoint — `/healthcheck` — that returns the current date and service status in JSON format.

## 🧩 Tech Stack
- Python 3.11  
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
   [https://sonya-api.onrender.com/healthcheck](https://sonya-api.onrender.com)

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
