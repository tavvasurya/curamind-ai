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

---

# 🎓 Conclusion

CuraMind AI demonstrates a production-style healthcare SaaS architecture integrating secure authentication, medical data management, and AI-powered diagnostic capabilities with explainable visualization.

This project represents a complete end-to-end healthcare AI system from authentication to AI prediction and frontend visualization.