from unittest.mock import AsyncMock

import pytest
from httpx import AsyncClient

from app.application.dtos.post_dto import PostDetailDto, PostDto
from app.application.dtos.user_dto import UserDto
from app.application.services.post_service import PostService
from app.core.dependencies import get_post_service
from app.domain.exceptions import NotFoundError
from app.main import app


@pytest.mark.asyncio
async def test_get_post_with_author(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=PostService)
    mock_service.get_post.return_value = PostDetailDto(
        external_id=10,
        user_external_id=1,
        title="Hello",
        body="World",
        views=100,
        tags=["life"],
        reactions={"likes": 5, "dislikes": 1},
        author=UserDto(
            external_id=1,
            first_name="Emily",
            last_name="Johnson",
            email="emily@example.com",
            username="emilys",
            image="https://example.com/emily.png",
            role="admin",
        ),
    )

    app.dependency_overrides[get_post_service] = lambda: mock_service
    try:
        response = await client.get("/api/v1/posts/10")
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Hello"
    assert data["author"]["username"] == "emilys"


@pytest.mark.asyncio
async def test_create_post_user_not_found(client: AsyncClient) -> None:
    mock_service = AsyncMock(spec=PostService)
    mock_service.create_post.side_effect = NotFoundError("User 999 not found")

    app.dependency_overrides[get_post_service] = lambda: mock_service
    try:
        response = await client.post(
            "/api/v1/posts",
            json={
                "user_external_id": 999,
                "title": "New post",
                "body": "Content",
            },
        )
    finally:
        app.dependency_overrides.clear()

    assert response.status_code == 404
    assert response.json() == {"detail": "User 999 not found"}
