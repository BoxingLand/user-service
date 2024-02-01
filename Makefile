#!/usr/bin/make

include .env.local


run:
	python -m app

up-local:
	docker compose -f docker-compose.local.yaml --env-file .env.local up -d

down-local:
	docker compose -f docker-compose.local.yaml down

yoyo-init:
	yoyo init --database postgresql+psycopg://$(DATABASE_USER):$(DATABASE_PASSWORD)@$(DATABASE_HOST):$(DATABASE_PORT)/$(DATABASE_NAME) migrations

ruff:
	ruff check app

grpc:
	python3 -m grpc_tools.protoc -I./app/protos --python_out=. --pyi_out=. --grpc_python_out=. ./app/protos/user.proto
