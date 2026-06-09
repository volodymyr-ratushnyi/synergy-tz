from abc import ABC, abstractmethod

from app.domain.repositories.post_repository import PostRepository
from app.domain.repositories.user_repository import UserRepository


class UnitOfWork(ABC):
    @property
    @abstractmethod
    def users(self) -> UserRepository:
        """User repository bound to the current unit of work."""

    @property
    @abstractmethod
    def posts(self) -> PostRepository:
        """Post repository bound to the current unit of work."""

    @abstractmethod
    async def commit(self) -> None:
        """Persist all changes made within the unit of work."""

    @abstractmethod
    async def rollback(self) -> None:
        """Discard all changes made within the unit of work."""

    async def __aenter__(self) -> "UnitOfWork":
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type is not None:
            await self.rollback()
        else:
            await self.commit()
