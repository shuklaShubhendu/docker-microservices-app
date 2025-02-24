# Microservices Application with Docker Compose 🚀

**📅 Date:** February 24, 2025

---

## 🏗 Introduction

This project demonstrates a **microservices-based application** built using **Docker** and **Docker Compose**. The application comprises three core services:

- **🌐 Web Service (Flask App)** - Handles HTTP requests and provides a user interface.
- **⚙️ Worker Service (Celery & Redis)** - Processes background tasks asynchronously.
- **🗄 Database Service (PostgreSQL)** - Stores persistent data.
- **🚀 Redis (Broker)** - Facilitates message communication for task management.

🛠 This setup showcases containerization, orchestration, and microservices architecture skills.

![Microservices Architecture](https://via.placeholder.com/800x400.png?text=Microservices+Architecture)

---

## ✨ Features

✅ **Microservices Architecture** - Independent and scalable services.
✅ **Dockerized Services** - Ensures consistency across environments.
✅ **Docker Compose for Orchestration** - Simplifies multi-container management.
✅ **Asynchronous Processing** - Uses Celery and Redis for task management.
✅ **Data Persistence** - Ensures database durability via Docker volumes.
✅ **Web UI** - Flask-based interface for user interactions.
✅ **Custom Image Names** - Prefixes container names with `ABCD123`.
✅ **Exposed Web Service** - Available at [http://localhost:8080](http://localhost:8080).
✅ **Verified Communication** - Logs and interactions ensure container connectivity.

---

## 🛠 Skills Demonstrated

- 🏗 **Microservices Design** - Independent, loosely coupled services.
- 🐳 **Docker & Docker Compose** - Containerization & multi-container orchestration.
- 🌍 **Flask Web Development** - Backend web service implementation.
- 📩 **Celery for Async Tasks** - Background job processing.
- 🔥 **Redis as Message Broker** - Efficient task management.
- 🗄 **PostgreSQL Database** - Persistent data storage.
- 🔌 **Container Networking** - Communication between services.
- 📜 **Log Management** - Monitoring application behavior.

---

## 📊 Architecture Diagram

```plaintext
+-------------------+      +--------------------+      +---------------------+
| 🌐 Web Service    | <---> | 🔥 Redis (Broker)  | <---> | ⚙️ Worker Service   |
| (Flask App)       |      |                    |      | (Celery Worker)     |
| - Exposes port 8080 |    +--------------------+      | - Background Tasks  |
+-------------------+                                  +---------------------+
        |
        v
+-------------------+
| 🗄 Database Service |
| (PostgreSQL)      |
| - Persistent Data |
+-------------------+
```

---

## 🚀 Getting Started

### 📌 Prerequisites

- **🐳 Docker** - Install from [Docker Desktop](https://www.docker.com/products/docker-desktop).
- **📦 Docker Compose** - Verify with:
  ```sh
  docker-compose --version
  ```

### 📥 Installation & Setup

1️⃣ **Clone the repository (or create files manually):**

```sh
git clone <your_repository_url>
cd microservices-app
```

📂 Ensure the file structure:

```plaintext
microservices-app/
├── docker-compose.yml
├── web-service/
│   ├── Dockerfile
│   ├── app.py
│   ├── requirements.txt
│   └── templates/
│       └── index.html
└── worker-service/
    ├── Dockerfile
    ├── requirements.txt
    └── worker.py
```

2️⃣ **Build Docker Images:**

```sh
docker-compose build
```

3️⃣ **Start the Application:**

```sh
docker-compose up -d
```

---

## 🔍 Verification

### 🌐 Access Web Service

📌 Open [http://localhost:8080](http://localhost:8080) in your browser. You should see:
- "Hello from Web Service!" 🎉
- Your Name 🏷️
- Your Roll Number 🆔
- Your Bio 📜
- Web Service Container ID 🔢
- Current Time ⏳

### 📜 Check Logs

- **Web Service Logs:**
  ```sh
  docker-compose logs web
  ```
- **Worker Service Logs:**
  ```sh
  docker-compose logs worker
  ```
- **Database Logs:**
  ```sh
  docker-compose logs db
  ```
- **Redis Logs:**
  ```sh
  docker-compose logs redis
  ```

### 🔎 Check Running Containers

```sh
docker ps
```

You should see the following running services:
- `abcd123-web-service` 🌐
- `abcd123-worker-service` ⚙️
- `postgres:13` 🗄
- `redis:latest` 🔥

---

## 📂 Repository Structure

```plaintext
microservices-app/
├── docker-compose.yml         # Docker Compose file
├── web-service/               # Web Service Directory
│   ├── Dockerfile             # Web Service Dockerfile
│   ├── app.py                 # Flask Application
│   ├── requirements.txt       # Dependencies
│   └── templates/             # HTML Files
│       └── index.html         # Web UI
└── worker-service/            # Worker Service Directory
    ├── Dockerfile             # Worker Dockerfile
    ├── requirements.txt       # Dependencies
    └── worker.py              # Celery Worker Code
```

---

## 📤 Submission Details

📌 Submit the following:

1️⃣ **Dockerfiles:**
   - `web-service/Dockerfile`
   - `worker-service/Dockerfile`

2️⃣ **docker-compose.yml** file 📜

3️⃣ **Git Repository Link** 📂
   - `web-service/app.py`
   - `worker-service/worker.py`
   - `web-service/templates/index.html`

4️⃣ **Screenshots in a PDF:** 📸
   - `docker-compose build` output
   - `docker-compose up -d` output
   - `docker-compose logs web`
   - `docker-compose logs worker`
   - `docker-compose logs db`
   - `docker ps` output
   - Web Service UI (localhost:8080)

---

## 📜 License

🔗 [MIT License](https://opensource.org/licenses/MIT)

---

## 📧 Contact

📩 **Shubhendu Shukla - shuklashubhendu6@gmail.com**

---
