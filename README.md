# CuraMind AI – Intelligent Healthcare Diagnostic SaaS

## 🏥 Project Overview

CuraMind AI is a secure, AI-powered healthcare SaaS platform designed to assist doctors and patients with:

- Role-based authentication
- Secure medical record management
- Appointment scheduling
- AI-powered disease prediction from medical scans
- Heatmap-based explainable AI visualization

This project demonstrates a full-stack healthcare system integrating Django, JWT authentication, background AI processing using Celery, and PyTorch-based medical image analysis.

---

# 📅 Week-1: Planning & Secure Backend Foundation

## 🔐 Authentication & Security
- Custom User Model (Doctor / Patient)
- JWT Authentication (Access & Refresh Tokens)
- Secure password hashing
- Role-Based Access Control (RBAC)
- Protected API endpoints

## 🗂 Backend Architecture
- Django + Django REST Framework
- Modular App Structure:
  - `users` → Authentication & roles
  - `records` → Medical records & appointments

---

# 📅 Week-2: Medical Records & Appointment System

## 📅 Appointment Management
- Doctors can create appointments
- Patients linked to doctors
- Appointment status tracking:
  - Scheduled
  - Completed
  - Cancelled

## 📁 Secure Medical Record Upload
- Doctors upload medical scan images
- File upload support (FileField)
- Stored in `media/medical_files/`
- Timestamp tracking (`uploaded_at`)
- Doctor automatically assigned from logged-in user

## 🔒 Role Enforcement
- Only authenticated users can access endpoints
- Doctor-only actions enforced in backend
- Patients can view only their own records

---

# 📅 Week-3: AI Integration & Explainable Diagnostics

## 🤖 AI Disease Prediction
- Integrated PyTorch ResNet18 model
- Image preprocessing (224x224 resize)
- AI class prediction
- Predicted class index mapped to disease categories:
  - Normal
  - Pneumonia
  - Tuberculosis
  - Lung Cancer
  - Fracture

## 🔥 Explainable AI (Heatmap Visualization)
- Heatmap generated using Matplotlib
- Overlay visualization on uploaded scan
- Stored in `media/heatmaps/`
- Returned via API endpoint
- Displayed in frontend UI

## ⚙ Background Processing with Celery
- AI processing runs asynchronously
- Non-blocking API responses
- Scalable backend design
---
# 🛠 Tech Stack

## Backend
- Django
- Django REST Framework
- SimpleJWT
- Celery
- SQLite (Development)
- Python 3.10+

## AI & Processing
- PyTorch
- Torchvision
- Pillow
- NumPy
- Matplotlib

## Frontend
- HTML
- CSS
- JavaScript (Fetch API)

---

# 🔐 Authentication APIs

## Register User
`POST /api/users/register/`

Example:
```json
{
  "username": "doctor1",
  "password": "password123",
  "role": "doctor"
}
```

---

## Login (JWT)
`POST /api/token/`

Response:
```json
{
  "refresh": "xxxxx",
  "access": "xxxxx"
}
```

---

## Refresh Token
`POST /api/token/refresh/`

---

# 📁 Medical Record APIs

## Upload Medical Record (Doctor Only)
`POST /api/records/upload/`

Form Data:
- patient → Patient ID
- diagnosis → "Fever"
- file → Upload scan image

Requires Header:
```
Authorization: Bearer <access_token>
```

---

## Check AI Status
`GET /api/records/ai-status/<record_id>/`

Example Response:
```json
{
  "ai_processed": true,
  "ai_prediction": "Fracture",
  "heatmap_image": "http://127.0.0.1:8000/media/heatmaps/heatmap_6.png"
}
```

---

# 📅 Appointment APIs

## Create Appointment
`POST /api/records/appointments/create/`

## View Appointments
`GET /api/records/appointments/`

---

# 🚀 How to Run Locally

## 1️⃣ Activate Virtual Environment

Windows:
```
venv\Scripts\activate
```

Mac/Linux:
```
source venv/bin/activate
```

---

## 2️⃣ Install Dependencies

```
pip install -r requirements.txt
```

---

## 3️⃣ Run Migrations

```
python manage.py makemigrations
python manage.py migrate
```

---

## 4️⃣ Start Django Server

```
python manage.py runserver
```

---

## 5️⃣ Start Celery Worker (Important)

```
celery -A curemind worker -l info
```

---

# 📦 requirements.txt

```
Django>=3.2,<6.0
djangorestframework
djangorestframework-simplejwt
django-cors-headers
python-dotenv
celery
torch
torchvision
Pillow
matplotlib
numpy
```

---

# 🎯 Key Achievements

- Secure JWT Authentication
- Role-Based Authorization
- Medical File Upload System
- Asynchronous AI Processing
- Deep Learning Integration
- Heatmap Explainable AI Visualization
- Full-Stack Healthcare SaaS Prototype

---

# 📌 Future Enhancements

- Real medical dataset training
- Grad-CAM heatmap implementation
- Confidence score display
- PostgreSQL production database
- Docker containerization
- AWS cloud deployment
- Patient dashboard
- Admin analytics panel

📅 Week-4 Implementation – Dockerized Deployment & Scalable AI Processing
🐳 Week-4 Overview

In Week-4, CuraMind AI was upgraded from a local development setup to a containerized, production-style architecture using Docker. The system now runs as multiple isolated services with asynchronous AI processing powered by Celery and Redis.

This week focused on:

Containerization of Django backend

Integration of Redis as message broker

Running Celery worker inside Docker

Service orchestration using Docker Compose

Environment-based configuration

Production-ready architecture design

🏗 Dockerized System Architecture

The application is structured into independent services:

Service	Purpose
web	Django backend application
redis	Message broker for Celery
celery	Background worker for AI tasks
db	SQLite (development)

🚀 Improvements Achieved in Week-4

Fully containerized backend

Asynchronous AI task execution

Clean microservice-style architecture

Redis-based message queue system

Background worker scalability

Environment-based configuration

Production-ready setup

🔐 Security & Scalability Enhancements

Secure environment variables handling

Decoupled services for better fault isolation

Celery worker scaling capability

Non-blocking AI processing

Modular and deployment-ready structure

📦 Technologies Used in Week-4

Docker

Docker Compose

Redis

Celery

Django REST Framework

PyTorch (AI Model)

SQLite (Development DB)

🎯 Outcome of Week-4

By the end of Week-4, CuraMind AI evolved from a locally running backend system into a containerized, scalable healthcare SaaS platform capable of handling asynchronous AI diagnostics efficiently.

The system now supports:

Secure authentication

Medical scan uploads

Background AI processing

Heatmap generation

Docker-based deployment

Service isolation and scalability


🎓 Conclusion
Week-4 successfully transformed CuraMind AI into a production-oriented architecture using Docker, Celery, and Redis. The implementation ensures scalability, maintainability, and efficient AI processing through asynchronous task execution.

This milestone demonstrates the transition from a development-level healthcare backend to a structured, deployment-ready SaaS system built with modern DevOps practices.
