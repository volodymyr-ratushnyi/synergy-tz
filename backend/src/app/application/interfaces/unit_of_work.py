from abc import ABC, abstractmethod


class UnitOfWork(ABC):
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
