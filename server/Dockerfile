FROM python:3.14.7-trixie

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# For local development:
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# For production environment
# CMD ["gunicorn", "ecom_proj.wsgi", "--bind", "0.0.0.0:8000"]