FROM python:3.9
ENV PYTHONBUFFERED 1

WORKDIR /app
COPY requirements.txt /app/

RUN pip install -r requirements.txt

COPY . /app

WORKDIR /api

CMD python manage.py runserver 0.0.0.0:8080