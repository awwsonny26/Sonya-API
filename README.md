# Sonya-API

A simple REST API built with **Node.js**, containerized with **Docker**, and using **Prisma ORM** with **PostgreSQL**.

## 🚀 Project Overview
This project was created as part of the *Server-Side Software Technologies* course.  
It implements a minimal web service with endpoints for managing **Users**, **Categories**, and **Records** (expenses).

## 🧩 Tech Stack
- Node.js 20  
- Express.js  
- Prisma ORM  
- PostgreSQL  
- Joi (validation)  
- Docker / Docker Compose

## 📦 Installation (Local)

1. **Install dependencies**
   ```bash
   npm install
   ```

2. **Configure environment variables**
   Create a file named `.env` in the project root with the following content:
   ```env
   DATABASE_URL="postgresql://sonya_user:sonya_pass@localhost:5432/sonya_db?schema=public"
   PORT=8080
   ```

3. **Generate Prisma client and apply migrations**
   ```bash
   npx prisma generate
   npx prisma migrate dev --name init
   ```

4. **Run locally**
   ```bash
   npm run dev
   ```

5. **Check health endpoint**
   ```bash
   curl http://localhost:8080/health
   ```

   Expected response:
   ```json
   {
     "status": "ok"
   }
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
The app can be easily deployed to **Render** or any Docker-compatible hosting service.

1. Push the project to GitHub.  
2. Create a new **Web Service** on [render.com](https://render.com).  
3. Connect the GitHub repo — Render will detect the Dockerfile automatically.  
4. Once deployed, visit your deployment URL and check `/health`.

## ✅ Example Response
```json
{
  "status": "ok"
}
```

---

> **Author:** Novakivska Sofia  
> **Group:** IO-35  

# 📚 Lab 2 — Expense Tracker API

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

## 📚 Lab 3 — Expense Tracker API

### Endpoints
**Users**
- `POST /users` — create `{ "name": "Alice" }` → 201
- `GET /users/{id}` — get by id → 200/404
- `DELETE /users/{id}` — delete → 204/404
- `GET /users` — list → 200

**Categories**
- `POST /categories` — create `{ "title": "Food", "isGlobal": true }` → 201
- `GET /categories` — list → 200
- `DELETE /categories/{id}` — delete → 204/404

**Records**
- `POST /records` — create `{ "userId": 1, "categoryId": 1, "amount": 99.5, "createdAt"?: ISO8601 }`  
  Validates that `userId` and `categoryId` exist. → 201/400
- `GET /records` — list all → 200
- `DELETE /records/{id}` — delete → 204/404

### 🧪 Postman
You can import the Postman collection for automated testing:
- `Sonya-Lab3.postman_collection.json`

Then select the appropriate environment (`Local` or `Production`) and run the test flow.

---

### ▶️ Run locally (development)
```bash
npm run dev
```

### 🐳 Docker (production)
```bash
docker compose up --build
```

### 🌐 Deployment
The app is ready for Docker-based deployment (e.g., Render, Railway, Fly.io).

---

> **Lab 3:** Node.js Implementation — Variant 2 (User-defined categories)
