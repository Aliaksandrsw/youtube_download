# Использование базового образа Python
FROM python:3.11.0-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
RUN apk update && apk add --no-cache \
    ffmpeg \
    gcc \
    musl-dev \
    python3-dev \
    libffi-dev \
    postgresql-dev


# copy project
COPY . .
