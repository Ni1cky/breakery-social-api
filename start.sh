#! /bin/sh

alembic upgrade head
uvicorn api:app --host 0.0.0.0 --port 80
