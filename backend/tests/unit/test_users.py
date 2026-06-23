from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient

from app.application.dtos.pagination import PaginatedResultDto
from app.application.dtos.user_dto import PostSummaryDto, UserDetailDto, UserDto
from app.application.services.user_service import UserService
from app.core.dependencies import get_user_service
from app.domain.exceptions import NotFoundError
from app.main import app


@pytest.mark.asyncio
async def test_list_users(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=UserService)
    mock_service.list_users.return_value = PaginatedResultDto(
        items=[
            UserDto(
                external_id=1,
                first_name="Emily",
                last_name="Johnson",
                email="emily@example.com",
                username="emilys",
                image="https://example.com/emily.png",
                role="admin",
            )
        ],
        total=1,
        offset=0,
        limit=20,
    )

    app.dependency_overrides[get_user_service] = lambda: mock_service
    try:
        response = await client.get("/api/v1/users?sort_by=first_name&sort_order=asc")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    data = response.json()
    assert data["total"] == 1
    assert data["items"][0]["first_name"] == "Emily"
    mock_service.list_users.assert_awaited_once()


@pytest.mark.asyncio
async def test_list_users_invalid_sort_by(client: AsyncClient) -> None:
    response = await client.get("/api/v1/users?sort_by=not_a_field")

    assert response.status_code == 422


@pytest.mark.asyncio
async def test_get_user_with_posts(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=UserService)
    mock_service.get_user.return_value = UserDetailDto(
        external_id=1,
        first_name="Emily",
        last_name="Johnson",
        email="emily@example.com",
        username="emilys",
        image="https://example.com/emily.png",
        role="admin",
        posts=[PostSummaryDto(external_id=10, title="Hello", views=100)],
    )

    app.dependency_overrides[get_user_service] = lambda: mock_service
    try:
        response = await client.get("/api/v1/users/1")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    data = response.json()
    assert data["external_id"] == 1
    assert len(data["posts"]) == 1
    assert data["posts"][0]["title"] == "Hello"


@pytest.mark.asyncio
async def test_get_user_not_found(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=UserService)
    mock_service.get_user.side_effect = NotFoundError("User 999 not found")

    app.dependency_overrides[get_user_service] = lambda: mock_service
    try:
        response = await client.get("/api/v1/users/999")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 404
    assert response.json() == {"detail": "User 999 not found"}
