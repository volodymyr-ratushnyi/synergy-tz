from sqlalchemy import delete, func, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.post import Post
from app.domain.repositories.post_repository import PostRepository
from app.infrastructure.persistence.mappers import to_post_entity
from app.infrastructure.persistence.models.post_model import PostModel

POST_SORT_FIELDS = {
    "external_id": PostModel.external_id,
    "title": PostModel.title,
    "views": PostModel.views,
    "user_external_id": PostModel.user_external_id,
}


class SqlAlchemyPostRepository(PostRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def upsert_many(self, posts: list[Post]) -> int:
        if not posts:
            return 0

        values = [
            {
                "external_id": post.external_id,
                "user_external_id": post.user_external_id,
                "title": post.title,
                "body": post.body,
                "views": post.views,
                "tags": post.tags,
                "reactions": post.reactions,
            }
            for post in posts
        ]

        stmt = insert(PostModel).values(values)
        stmt = stmt.on_conflict_do_update(
            index_elements=["external_id"],
            set_={
                "user_external_id": stmt.excluded.user_external_id,
                "title": stmt.excluded.title,
                "body": stmt.excluded.body,
                "views": stmt.excluded.views,
                "tags": stmt.excluded.tags,
                "reactions": stmt.excluded.reactions,
            },
        )
        await self._session.execute(stmt)
        return len(posts)

    async def get_by_id(self, external_id: int) -> Post | None:
        result = await self._session.execute(
            select(PostModel).where(PostModel.external_id == external_id)
        )
        model = result.scalar_one_or_none()
        return to_post_entity(model) if model else None

    async def list(
        self,
        *,
        offset: int,
        limit: int,
        sort_by: str,
        sort_order: str,
        user_external_id: int | None = None,
    ) -> list[Post]:
        sort_column = POST_SORT_FIELDS.get(sort_by, PostModel.external_id)
        order = sort_column.asc() if sort_order == "asc" else sort_column.desc()

        query = select(PostModel).order_by(order).offset(offset).limit(limit)
        if user_external_id is not None:
            query = query.where(PostModel.user_external_id == user_external_id)

        result = await self._session.execute(query)
        return [to_post_entity(model) for model in result.scalars().all()]

    async def list_by_user(self, user_external_id: int) -> list[Post]:
        result = await self._session.execute(
            select(PostModel)
            .where(PostModel.user_external_id == user_external_id)
            .order_by(PostModel.external_id.asc())
        )
        return [to_post_entity(model) for model in result.scalars().all()]

    async def count(self, user_external_id: int | None = None) -> int:
        query = select(func.count()).select_from(PostModel)
        if user_external_id is not None:
            query = query.where(PostModel.user_external_id == user_external_id)
        result = await self._session.execute(query)
        return result.scalar_one()

    async def get_next_external_id(self) -> int:
        result = await self._session.execute(select(func.max(PostModel.external_id)))
        max_id = result.scalar_one_or_none()
        return (max_id or 0) + 1

    async def create(self, post: Post) -> Post:
        model = PostModel(
            external_id=post.external_id,
            user_external_id=post.user_external_id,
            title=post.title,
            body=post.body,
            views=post.views,
            tags=post.tags,
            reactions=post.reactions,
        )
        self._session.add(model)
        await self._session.flush()
        return to_post_entity(model)

    async def update(self, post: Post) -> Post | None:
        result = await self._session.execute(
            select(PostModel).where(PostModel.external_id == post.external_id)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None

        model.user_external_id = post.user_external_id
        model.title = post.title
        model.body = post.body
        model.views = post.views
        model.tags = post.tags
        model.reactions = post.reactions
        await self._session.flush()
        return to_post_entity(model)

    async def delete(self, external_id: int) -> bool:
        result = await self._session.execute(
            delete(PostModel).where(PostModel.external_id == external_id)
        )
        return result.rowcount > 0

    async def delete_by_user(self, user_external_id: int) -> int:
        result = await self._session.execute(
            delete(PostModel).where(PostModel.user_external_id == user_external_id)
        )
        return result.rowcount
