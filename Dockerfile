FROM ghcr.io/astral-sh/uv:0.2.33 as uv
FROM python:3.12.4-alpine3.20 as build

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV VIRTUAL_ENV=/usr/local

RUN --mount=from=uv,source=/uv,target=./uv \
    ./uv venv /opt/venv


ENV VIRTUAL_ENV=/opt/venv
ENV PATH="/opt/venv/bin:$PATH"

# Установка инструментов для сборки и необходимых библиотек
RUN apk add --no-cache gcc musl-dev libc-dev zlib-dev

COPY requirements/ /

ENV BUILD_ENVIRONMENT=local

RUN --mount=type=cache,target=/root/.cache/uv \
    --mount=from=uv,source=/uv,target=./uv \
    ./uv pip install  -r ${BUILD_ENVIRONMENT}.txt

WORKDIR /app/

COPY / /app/
ENV PYTHONPATH "${PYTHONPATH}:/app/"