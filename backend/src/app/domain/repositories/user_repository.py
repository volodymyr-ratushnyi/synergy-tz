from abc import ABC, abstractmethod

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def upsert_many(self, users: list[User]) -> int:
        """Insert or update users. Returns the number of affected rows."""

    @abstractmethod
    async def get_by_id(self, external_id: int) -> User | None:
        """Return a user by external id."""

    @abstractmethod
    async def list(
        self,
        *,
        offset: int,
        limit: int,
        sort_by: str,
        sort_order: str,
    ) -> list[User]:
        """Return a paginated, sorted list of users."""

    @abstractmethod
    async def count(self) -> int:
        """Return total number of users."""

    @abstractmethod
    async def get_next_external_id(self) -> int:
        """Return the next available external id for a new user."""

    @abstractmethod
    async def create(self, user: User) -> User:
        """Create a new user."""

    @abstractmethod
    async def update(self, user: User) -> User | None:
        """Update an existing user. Returns None if not found."""

    @abstractmethod
    async def delete(self, external_id: int) -> bool:
        """Delete a user. Returns True if deleted."""
