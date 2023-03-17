FROM python:3.10

#  Configure Poetry
ENV POETRY_VERSION=1.1.13 \ 
    POETRY_HOME=/opt/poetry \
    POETRY_VENV=/opt/poetry-venv \
    POETRY_CACHE_DIR=/opt/.cache

# Install poetry separated from system interpreter
RUN python3 -m venv $POETRY_VENV \
    && $POETRY_VENV/bin/pip install -U pip setuptools \
    && $POETRY_VENV/bin/pip install poetry==${POETRY_VERSION}

ENV PATH="${PATH}:${POETRY_VENV}/bin"

COPY ./src ./src
COPY ./README.md ./
COPY pyproject.toml poetry.lock ./
RUN poetry install

COPY . .

EXPOSE 5001

ENTRYPOINT entrypoint.sh


