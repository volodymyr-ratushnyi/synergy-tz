# Synergy Backend

FastAPI backend with Clean Architecture and CQRS.

## Development

```bash
uv sync
uv run uvicorn app.main:app --reload --app-dir src
```

## Tests

```bash
uv run pytest
```

## Migrations

```bash
uv run alembic revision --autogenerate -m "description"
uv run alembic upgrade head
```
