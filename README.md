# Backend – API RESTful con Django Rest Framework (DRF) para gestionar las tareas.

## Tecnología
- Python 3.10, Django 5.2, DRF, Simple JWT, PostgreSQL, Docker

## 🛠️ Requisitos
- Docker y Docker Compose
- Acceso a puerto 8000 y 5432

## 🔧 Instalación local
1. Clona el repo.
2. Sitúate en `backend/`.
3. Ejecuta:
   ```bash
   docker-compose up -d --build

4. Entra al container backend y ejecuta:

- docker-compose exec backend python manage.py migrate
- docker-compose exec backend python manage.py createsuperuser

5.Ya puedes usar la API:

Registro: POST /api/registro/

Login: POST /api/token/

CRUD tareas en /api/tareas/