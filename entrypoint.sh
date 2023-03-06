#!/bin/bash

poetry run alembic upgrade head
poetry run gunicorn -w 4 --bind $FLASK_HOST:$FLASK_PORT src.portfolio.wsgi:app