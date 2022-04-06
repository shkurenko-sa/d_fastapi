FROM python:3.10.2-alpine3.15

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /app
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt

RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev 
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY . /app/
