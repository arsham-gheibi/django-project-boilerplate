FROM python:3.12.6-alpine3.20
LABEL maintainer="Arsham Gheibi"

ENV PYTHONUNBUFFERED=1 \
    POETRY_HOME=/poetry \
    POETRY_VIRTUALENVS_CREATE=false \
    PATH="/scripts:/poetry/bin:$PATH"

COPY ./pyproject.toml /pyproject.toml
COPY ./poetry.lock /poetry.lock
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client postgresql-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
    build-base musl-dev linux-headers curl && \
    curl -sSL https://install.python-poetry.org | python - && \
    poetry install --no-root --no-cache --no-ansi --no-interaction \
    $(if [ "$DEV" = "false" ]; then echo "--only main"; fi) && \
    apk del .tmp-build-deps && \
    adduser \
    --disabled-password \
    --no-create-home \
    django-user && \
    mkdir -p /vol/web/media /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    chmod +x /scripts

USER django-user

CMD ["run.sh"]
