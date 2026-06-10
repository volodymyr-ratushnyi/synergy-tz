from __future__ import annotations

from abc import ABC, abstractmethod

from app.domain.entities.post import Post


class PostRepository(ABC):
    @abstractmethod
    async def upsert_many(self, posts: list[Post]) -> int:
        """Insert or update posts. Returns the number of affected rows."""

    @abstractmethod
    async def get_by_id(self, external_id: int) -> Post | None:
        """Return a post by external id."""

    @abstractmethod
    async def list(
        self,
        *,
        offset: int,
        limit: int,
        sort_by: str,
        sort_order: str,
        user_external_id: int | None = None,
    ) -> list[Post]:
        """Return a paginated, sorted list of posts."""

    @abstractmethod
    async def list_by_user(self, user_external_id: int) -> list[Post]:
        """Return all posts for a given user."""

    @abstractmethod
    async def count(self, user_external_id: int | None = None) -> int:
        """Return total number of posts, optionally filtered by user."""

    @abstractmethod
    async def get_next_external_id(self) -> int:
        """Return the next available external id for a new post."""

    @abstractmethod
    async def create(self, post: Post) -> Post:
        """Create a new post."""

    @abstractmethod
    async def update(self, post: Post) -> Post | None:
        """Update an existing post. Returns None if not found."""

    @abstractmethod
    async def delete(self, external_id: int) -> bool:
        """Delete a post. Returns True if deleted."""

    @abstractmethod
    async def delete_by_user(self, user_external_id: int) -> int:
        """Delete all posts for a user. Returns the number of deleted posts."""
