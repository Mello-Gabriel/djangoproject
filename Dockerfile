FROM python:3.12-slim-bookworm

WORKDIR /app

ENV PYTHONUNBUFFERED 1

COPY pyproject.toml uv.lock ./ 

RUN apt-get update && apt-get install -y postgresql-client && rm -rf /var/lib/apt/lists/*
RUN pip install uv && uv pip install --system -r pyproject.toml

COPY . /app

EXPOSE 8000

CMD ["./run_django.sh"]
