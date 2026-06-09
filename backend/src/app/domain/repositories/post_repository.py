from abc import ABC, abstractmethod

from app.domain.entities.post import Post


class PostRepository(ABC):
    @abstractmethod
    async def upsert_many(self, posts: list[Post]) -> int:
        """Insert or update posts. Returns the number of affected rows."""
