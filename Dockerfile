FROM python:3.11.4-alpine

EXPOSE 8000

WORKDIR /app

COPY ./pyproject.toml ./poetry.lock ./create_yoyo_ini.sh /migrations/ /app/

RUN pip install --upgrade pip
RUN pip install poetry

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

RUN apk add --no-cache bash

COPY . ./
