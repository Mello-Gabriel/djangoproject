#!/usr/bin/env bash
# exit on error
set -o errexit

uv sync --frozen && uv cache prune --ci

python my_site/manage.py collectstatic --no-input
python my_site/manage.py migrate
