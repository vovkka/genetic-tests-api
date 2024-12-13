FROM python:3.12

WORKDIR /app

# Установка netcat для проверки доступности базы данных
RUN apt-get update && apt-get install -y netcat-traditional && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "genetic/manage.py", "runserver", "0.0.0.0:8000"] 