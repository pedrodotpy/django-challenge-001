FROM python:3.7

RUN adduser --disabled-password --no-create-home app

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

COPY requirements.txt .
COPY requirements-prod.txt .

RUN pip3 install --upgrade pip && \
    pip3 install -r requirements-prod.txt --no-cache-dir

RUN apt-get update && \
    apt-get install -y postgresql-client && \
    mkdir -p ./staticfiles

COPY . .

USER app

ENTRYPOINT ["sh", "./wait-for-postgres.sh", "db", "sh", "./docker-entrypoint.sh"]