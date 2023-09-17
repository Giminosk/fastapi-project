FROM python:3.11

WORKDIR /app

RUN pip install --upgrade pip \
  && pip install poetry

COPY ../pyproject.toml .
COPY ../poetry.lock .

RUN poetry config virtualenvs.create false
RUN poetry install --no-interaction --no-ansi

COPY ../.env .
COPY ../src ./src

EXPOSE 8000

ENV PYTHONPATH=/app

CMD ["python", "src/main.py"]
