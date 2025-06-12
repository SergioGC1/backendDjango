FROM python:3.10-slim

# Instala dependencias del sistema necesarias para psycopg2 y psql
RUN apt-get update \
 && apt-get install -y libpq-dev gcc postgresql-client \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copia solo requirements para aprovechar cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del código
COPY . /app

# Comando por defecto
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
