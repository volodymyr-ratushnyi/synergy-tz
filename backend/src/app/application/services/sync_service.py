from typing import Any

from app.application.dtos.sync_result_dto import SyncResultDto
from app.application.interfaces.unit_of_work import UnitOfWork
from app.domain.entities.post import Post
from app.domain.entities.user import User
from app.infrastructure.external.dummyjson_client import DummyJsonClient


class SyncService:
    def __init__(self, uow: UnitOfWork, client: DummyJsonClient) -> None:
        self._uow = uow
        self._client = client

    async def sync(self) -> SyncResultDto:
        users_data = await self._client.fetch_users()
        users = [_map_user(item) for item in users_data]
        users_count = await self._uow.users.upsert_many(users)

        posts_data = await self._client.fetch_posts()
        posts = [_map_post(item) for item in posts_data]
        posts_count = await self._uow.posts.upsert_many(posts)

        return SyncResultDto(users_count=users_count, posts_count=posts_count)


def _map_user(data: dict[str, Any]) -> User:
    return User(
        external_id=data["id"],
        first_name=data["firstName"],
        last_name=data["lastName"],
        email=data["email"],
        username=data["username"],
        image=data["image"],
        role=data["role"],
    )


def _map_post(data: dict[str, Any]) -> Post:
    return Post(
        external_id=data["id"],
        user_external_id=data["userId"],
        title=data["title"],
        body=data["body"],
        views=data.get("views", 0),
        tags=data.get("tags", []),
        reactions=data.get("reactions", {}),
    )
