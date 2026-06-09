from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.post import Post
from app.domain.repositories.post_repository import PostRepository
from app.infrastructure.persistence.models.post_model import PostModel


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
