# Synergy Backend

FastAPI backend with Clean Architecture.

## Development

```bash
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload --app-dir src
```

## Tests

```bash
uv run pytest
```

## Formatting

```bash
uv run black src tests
```

## Migrations

```bash
uv run alembic revision --autogenerate -m "description"
uv run alembic upgrade head
```

In Docker, migrations run automatically via the `migrate` service in root `docker-compose.yml`.
