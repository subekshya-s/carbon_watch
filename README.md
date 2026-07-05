# 🌿 Carbon Watch Nepal

> A satellite-based forest carbon monitoring platform for Nepal built with Django, PostGIS, Google Earth Engine, and React.

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Django](https://img.shields.io/badge/Django-6.0-success)
![PostGIS](https://img.shields.io/badge/PostGIS-3.4-green)
![React](https://img.shields.io/badge/React-Vite-61DAFB)
![License](https://img.shields.io/badge/License-MIT-yellow)

---

## 📖 About

Carbon Watch Nepal is a web application that estimates forest carbon information for Nepal's 77 districts using satellite imagery.

Users can:

- 🗺️ Select a district on an interactive map
- 🌍 Trigger satellite analysis
- 🌲 View land cover statistics
- 🌱 Estimate forest carbon stock
- 🤖 Read an AI-generated summary of the results

The project was developed as a capstone project for the **Code Rush Fellowship 2026**.

---

## ✨ Features

- User authentication using JWT
- Interactive Nepal district map
- PostGIS spatial database
- Google Earth Engine integration
- ESA WorldCover land cover analysis
- Forest carbon estimation
- AI-generated plain language summaries (Gemini)
- REST API with Swagger documentation
- CI/CD using GitHub Actions

---

## 🏗️ Project Architecture

```text
                React + Leaflet
                       │
                       ▼
            Django REST Framework
                       │
         ┌─────────────┴─────────────┐
         ▼                           ▼
 Google Earth Engine           PostgreSQL + PostGIS
         │                           │
         ▼                           ▼
 ESA WorldCover             Nepal District Boundaries
         │
         ▼
 Land Cover Statistics
         │
         ▼
 Carbon Estimation
         │
         ▼
 Gemini AI Summary
```

---

## 🛠️ Tech Stack

| Layer | Technology |
|--------|------------|
| Backend | Django 6 + Django REST Framework |
| Database | PostgreSQL 16 + PostGIS |
| Spatial ORM | django.contrib.gis |
| Authentication | JWT (SimpleJWT) |
| Satellite Analysis | Google Earth Engine |
| Land Cover Dataset | ESA WorldCover |
| AI Summary | Gemini API |
| Frontend | React + Vite + Leaflet |
| Charts | Recharts |
| Testing | pytest + pytest-django |
| Documentation | drf-spectacular (Swagger) |
| CI/CD | GitHub Actions |

---

# 📂 Repository Structure

```text
carbon_watch/

├── backend/
│   ├── accounts/
│   ├── analysis/
│   │   └── services/
│   │       └── earth_engine.py
│   ├── areaofintrest/
│   ├── config/
│   ├── data/
│   └── manage.py
│
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
│
├── .github/
│   └── workflows/
│       └── ci.yml
│
└── README.md
```

---

# 🌍 Workflow

```text
User selects district
          │
          ▼
Frontend sends request
          │
          ▼
POST /api/districts/{id}/analyze/
          │
          ▼
Google Earth Engine
          │
          ▼
Clip district boundary
          │
          ▼
ESA WorldCover Analysis
          │
          ▼
Land Cover Statistics
          │
          ▼
Carbon Estimation
          │
          ▼
Gemini AI Summary
          │
          ▼
Return results to frontend
```

---

# 📊 Current Progress

| Feature | Status |
|----------|--------|
| Backend API | ✅ |
| JWT Authentication | ✅ |
| District API | ✅ |
| PostGIS Integration | ✅ |
| Google Earth Engine Authentication | ✅ |
| District Geometry Conversion | ✅ |
| Interactive React Map | ✅ |
| Mock Analysis Pipeline | ✅ |
| Earth Engine Analysis | 🚧 In Progress |
| Carbon Estimation | 🚧 In Progress |
| Gemini AI Summary | 🚧 In Progress |
| Deployment | ⏳ Planned |

---

# 🚀 Installation

## Clone repository

```bash
git clone https://github.com/subekshya-s/carbon_watch.git

cd carbon_watch
```

---

## Backend

```bash
cd backend

python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt
```

Create a `.env`

```env
DB_PASSWORD=your_database_password
EE_PROJECT=your_google_cloud_project
```

Run migrations

```bash
python manage.py migrate

python manage.py load_districts

python manage.py runserver
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

# 📚 API Endpoints

| Method | Endpoint | Description |
|---------|----------|-------------|
| POST | `/api/accounts/register/` | Register user |
| POST | `/api/token/` | Login |
| POST | `/api/token/refresh/` | Refresh JWT |
| POST | `/api/accounts/logout/` | Logout |
| GET | `/api/districts/` | List districts |
| GET | `/api/districts/{id}/` | District details |
| POST | `/api/districts/{id}/analyze/` | Run analysis |
| GET | `/api/analyses/{id}/` | Analysis results |
| GET | `/swagger/` | Swagger UI |

---

# 🧪 Running Tests

```bash
pytest
```

---

# 📖 Documentation

Swagger documentation

```
http://localhost:8000/swagger/
```

---

# 📈 Future Improvements

- Real-time Earth Engine analysis
- Multi-year comparison (2018–2025)
- NDVI-based vegetation analysis
- Downloadable PDF reports
- Carbon trend visualization
- User dashboard
- Deployment on cloud infrastructure

---

# 👩‍💻 Author

**Subekshya Subedi**

Geomatics Engineering Graduate  
Tribhuvan University

Backend Developer | GIS Developer | Remote Sensing Enthusiast

GitHub: https://github.com/subekshya-s

---

# 🙏 Acknowledgements

- Code Rush Fellowship 2026
- Google Earth Engine
- ESA WorldCover
- Django
- React
- PostGIS
