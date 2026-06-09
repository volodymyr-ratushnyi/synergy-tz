# synergy-tz

Монорепозиторій з FastAPI бекендом (Clean Architecture + CQRS), React фронтендом (Feature-Sliced Design) та PostgreSQL. Усі сервіси запускаються через Docker Compose.

## Структура

```
synergy-tz/
├── backend/     # FastAPI + Clean Architecture + CQRS
├── frontend/    # React + FSD (Vite + TypeScript)
├── docker-compose.yml
└── .env.example
```

## Швидкий старт

1. Скопіюйте змінні оточення:

```bash
cp .env.example .env
```

2. Запустіть усі сервіси:

```bash
docker compose up --build
```

3. Відкрийте:

- Frontend: http://localhost:5173
- Backend API: http://localhost:8000
- API docs: http://localhost:8000/docs
- Health check: http://localhost:8000/api/v1/health

## Локальна розробка (без Docker)

### Backend

```bash
cd backend
uv sync
uv run uvicorn app.main:app --reload --app-dir src
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Тести (backend)

```bash
cd backend
uv run pytest
```

## Архітектура

### Backend (Clean Architecture + CQRS)

| Шар | Папка | Відповідальність |
|-----|-------|------------------|
| Domain | `domain/` | Entities, repository interfaces, domain exceptions |
| Application | `application/` | Commands, queries, DTOs, handler interfaces |
| Infrastructure | `infrastructure/` | SQLAlchemy, Unit of Work |
| Presentation | `presentation/` | FastAPI routers, Pydantic schemas |
| Core | `core/` | Config, DI, cross-cutting concerns |

### Frontend (Feature-Sliced Design)

```
app → pages → widgets → features → entities → shared
```

Імпорти дозволені лише з нижніх шарів. Кожен слайс експортує public API через `index.ts`.
