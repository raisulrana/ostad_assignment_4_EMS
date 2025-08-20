FROM python:3-slim

WORKDIR /app

COPY requirements.txt .

RUN apt-get update && apt-get install -y \
    build-essential \
    zlib1g-dev \
    libpq-dev \
    libffi-dev \
    && apt-get remove -y build-essential libpq-dev \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

RUN pip install -r requirements.txt

COPY . /app/    

EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]