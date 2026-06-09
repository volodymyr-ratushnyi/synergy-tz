from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient

from app.application.dtos.sync_result_dto import SyncResultDto
from app.application.services.sync_service import SyncService
from app.core.dependencies import get_sync_service
from app.core.exceptions import AppError
from app.main import app


@pytest.mark.asyncio
async def test_sync_success(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=SyncService)
    mock_service.sync.return_value = SyncResultDto(users_count=208, posts_count=251)

    app.dependency_overrides[get_sync_service] = lambda: mock_service
    try:
        response = await client.post("/api/v1/sync")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    assert response.json() == {"users_count": 208, "posts_count": 251}
    mock_service.sync.assert_awaited_once()


@pytest.mark.asyncio
async def test_sync_external_api_error(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=SyncService)
    mock_service.sync.side_effect = AppError(
        "External API returned 503 for /users",
        status_code=502,
    )

    app.dependency_overrides[get_sync_service] = lambda: mock_service
    try:
        response = await client.post("/api/v1/sync")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 502
    assert response.json() == {"detail": "External API returned 503 for /users"}
