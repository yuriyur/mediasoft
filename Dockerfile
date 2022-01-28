# syntax=docker/dockerfile:1
FROM debian:latest

ENV LANG=C.UTF-8 

WORKDIR /var/www/mediasoft
COPY . /var/www/mediasoft

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apt-get update
RUN apt-get install -y --no-install-recommends python3  python3-pip  python3-tk  gunicorn  gcc;  rm -rf /var/lib/apt/lists/*

CMD ["python3"]

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
