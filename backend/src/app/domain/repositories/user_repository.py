from abc import ABC, abstractmethod

from app.domain.entities.user import User


class UserRepository(ABC):
    @abstractmethod
    async def upsert_many(self, users: list[User]) -> int:
        """Insert or update users. Returns the number of affected rows."""
