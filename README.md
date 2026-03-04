# 🔒 CloudSec AI

AI-Powered Cloud Log Intelligence Platform

CloudSec AI is a full-stack security analytics platform that ingests cloud logs, performs anomaly detection using machine learning, and provides AI-powered contextual explanations for suspicious events.

This project demonstrates backend architecture, AI integration, authentication, database design, and cloud-ready deployment patterns.

---

## 🚀 Tech Stack

### 🔹 Backend
- FastAPI
- Python 3.11+
- SQLAlchemy
- PostgreSQL
- JWT Authentication (python-jose)
- Passlib (password hashing)

### 🔹 AI Layer
- IsolationForest (Scikit-learn)
- Feature Engineering
- OpenAI / AWS Bedrock (LLM explanations – upcoming)

### 🔹 Frontend (Planned)
- React + TypeScript
- TailwindCSS
- Axios
- Recharts

### 🔹 Cloud & DevOps
- Docker
- AWS ECS
- AWS RDS
- AWS S3
- AWS CloudFront
- Terraform (Infrastructure as Code)
- GitHub Actions CI/CD

---

## 🎯 Project Goal

CloudSec AI simulates a production-style cloud log monitoring system.

It performs:

1. Log ingestion via API  
2. Feature extraction  
3. Anomaly detection using ML  
4. Persistent scoring  
5. (Upcoming) LLM-based explanation of anomalies  

---

## 🏗️ Architecture

Client  
↓  
FastAPI Routes  
↓  
Service Layer  
↓  
Anomaly Detection Service  
↓  
Database (PostgreSQL)

### Layered Structure

app/  
 ├── models/  
 ├── schemas/  
 ├── routes/  
 ├── services/  
 ├── utils/  

- Routes → Thin controllers  
- Services → Business logic  
- Models → Database layer  
- Schemas → Validation layer  

---

## 🔐 Authentication

- JWT-based authentication  
- Secure password hashing (bcrypt)  
- Protected endpoints via dependency injection  

---

## 📊 Current Backend Features (Phase 1)

✅ User registration & login  
✅ JWT authentication  
✅ Log ingestion endpoint  
✅ Persistent anomaly scoring  
✅ IsolationForest anomaly detection  
✅ Clean service-layer architecture  

---

## Current Frontend Features (Not Implemented)

---

## Current Cloud and Devops Features (Not Implemented)

---

## 📜 Log Intelligence Pipeline

When a log is submitted:

1. Log stored in database  
2. Features extracted from message  
3. IsolationForest scoring executed  
4. anomaly_score stored  
5. is_anomaly flag stored  
6. Enriched log returned  

---

## 🗄️ Database Schema

### Users
- id  
- email (unique)  
- hashed_password  

### Logs
- id  
- message  
- level  
- created_at  
- anomaly_score  
- is_anomaly  
- explanation (nullable)  

---

## 🛠️ Running Locally

### 1️⃣ Install dependencies

pip install -r requirements.txt  

### 2️⃣ Setup PostgreSQL

Update `.env` with:

DATABASE_URL=postgresql://user:password@localhost/cloudsecai  
SECRET_KEY=your_secret_key  

### 3️⃣ Run backend

uvicorn app.main:app --reload  

Backend runs at:

http://127.0.0.1:8000  

Swagger Docs:

http://127.0.0.1:8000/docs  

---

## 🚀 Deployment

CloudSec AI is designed to be containerized and deployed on AWS using modern DevOps practices.

### 🔹 Docker (Containerization)

Build Docker image:

docker build -t cloudsec-ai-backend .  

Run container:

docker run -p 8000:8000 --env-file .env cloudsec-ai-backend  

This ensures consistent environments across development and production.

---

### 🔹 AWS Architecture (Planned Design)

Backend → AWS ECS (Fargate)  
Database → AWS RDS (PostgreSQL)  
Static assets → AWS S3  
CDN → AWS CloudFront  

Flow:

Client  
↓  
CloudFront  
↓  
ECS Service (FastAPI Container)  
↓  
RDS (PostgreSQL)

---

### 🔹 Infrastructure as Code (Terraform)

Infrastructure components can be provisioned using Terraform:

- ECS Cluster  
- Task Definitions  
- RDS Instance  
- Security Groups  
- IAM Roles  
- S3 Buckets  

Example command:

terraform init  
terraform plan  
terraform apply  

---

### 🔹 CI/CD (GitHub Actions)

Planned pipeline:

1. Push to main branch  
2. Run lint + tests  
3. Build Docker image  
4. Push to container registry  
5. Deploy to ECS  

This enables automated, production-ready deployments.

---

## 📌 API Endpoints

### Auth
- POST /auth/register  
- POST /auth/login  

### Logs
- POST /logs/upload  
- (Upcoming) GET /logs  
- (Upcoming) GET /logs/anomalies  

### AI (Upcoming)
- POST /ai/explain/{log_id}  

---

## 🧠 Future Enhancements

- LLM-based anomaly explanation  
- Log filtering & dashboard API  
- Role-based access control  
- Model retraining pipeline  
- Real-time streaming log ingestion  
- Frontend dashboard with visual analytics  

---

## 📈 Why This Project Matters

CloudSec AI demonstrates:

- Secure backend development  
- Clean layered architecture  
- ML model integration  
- Persistent AI scoring  
- Production-style API design  
- Cloud-native deployment planning  
- DevOps automation  

This project is designed to reflect real-world cloud security monitoring systems.

---

## 👤 Author

Built as a portfolio-grade system showcasing backend engineering and AI integration.
