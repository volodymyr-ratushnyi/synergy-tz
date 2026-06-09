# synergy-tz

Монорепозиторій: FastAPI backend (Clean Architecture), React frontend (Feature-Sliced Design), PostgreSQL. Дані users/posts синхронізуються з [DummyJSON](https://dummyjson.com), далі CRUD працює з локальною БД.

## Deployment (single command)

**Вимоги:** Docker і Docker Compose.

```bash
docker compose up --build
```

Файл `.env` **не обов'язковий** — у `docker-compose.yml` є дефолти для всіх змінних. Для кастомізації скопіюйте `.env.example` → `.env`.

При старті автоматично:

1. Піднімається PostgreSQL (з healthcheck)
2. Сервіс `migrate` виконує `alembic upgrade head`
3. Стартує backend (FastAPI)
4. Стартує frontend (Vite)

### Endpoints

| URL | Опис |
|-----|------|
| http://localhost:5173 | Frontend |
| http://localhost:8000/docs | Swagger UI |
| http://localhost:8000/api/v1/health | Health check |
| http://localhost:8000/api/v1/sync | `POST` — sync users/posts з DummyJSON |
| http://localhost:8000/api/v1/users | CRUD users |
| http://localhost:8000/api/v1/posts | CRUD posts |

### Перший запуск даних

Після `docker compose up` виконайте sync (один раз або при оновленні даних з DummyJSON):

```bash
curl -X POST http://localhost:8000/api/v1/sync
```

## Структура репозиторію

```
synergy-tz/
├── backend/          # FastAPI + Clean Architecture
├── frontend/         # React + FSD (Vite + TypeScript)
├── docker-compose.yml
└── .env.example
```

## Архітектура та ключові рішення

### Backend: Clean Architecture

Залежності спрямовані всередину: Presentation → Application → Domain; Infrastructure реалізує інтерфейси Domain.

| Шар | Папка | Відповідальність |
|-----|-------|------------------|
| Domain | `domain/` | Entities, repository interfaces, domain exceptions |
| Application | `application/` | Services, DTOs |
| Infrastructure | `infrastructure/` | SQLAlchemy repos, DummyJSON client, Unit of Work |
| Presentation | `presentation/` | FastAPI routes, Pydantic request/response schemas |
| Core | `core/` | Config, DI, cross-cutting concerns |

**Ключові рішення:**

- **Async-only I/O** — `httpx.AsyncClient`, SQLAlchemy async (`asyncpg`); без blocking calls у `async def`
- **Ідемпотентний sync** — `INSERT … ON CONFLICT DO UPDATE` за `external_id` (PK з DummyJSON)
- **Розділення schemas** — окремі Pydantic request/response; внутрішні DTO — dataclasses
- **Routes → Services → Repositories** — endpoints тонкі, бізнес-логіка в services
- **Unit of Work** — одна транзакція на HTTP-запит, auto-commit/rollback через DI
- **Помилки зовнішнього API** — timeout → 504, non-200 → 502 через `AppError`
- **Міграції в Compose** — окремий одноразовий сервіс `migrate` перед стартом backend

### Frontend: Feature-Sliced Design

```
app → pages → widgets → features → entities → shared
```

Імпорти лише з нижніх шарів. Public API кожного слайсу — через `index.ts`.

### API design

- REST під `/api/v1`
- List endpoints: `offset`, `limit`, `sort_by`, `sort_order` query params
- `GET /users/{id}` — user + related posts
- `GET /posts/{id}` — post + related author
- Config через env (`pydantic-settings`), CORS з `CORS_ORIGINS`

## Локальна розробка (без Docker)

### Backend

```bash
cd backend
uv sync
uv run alembic upgrade head
uv run uvicorn app.main:app --reload --app-dir src
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

### Тести

```bash
cd backend
uv run pytest
```

## Code formatting

**Python (Black):**

```bash
cd backend
uv run black src tests
```

**TypeScript (Prettier):**

```bash
cd frontend
npm run format
```

## Git

Репозиторій: https://github.com/volodymyr-ratushnyi/synergy-tz

Переконайтесь, що репозиторій **public** у налаштуваннях GitHub (Settings → General → Change repository visibility).
