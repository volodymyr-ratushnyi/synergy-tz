from abc import ABC, abstractmethod
from typing import TypeVar

Q = TypeVar("Q")
R = TypeVar("R")


class QueryHandler[Q, R](ABC):
    @abstractmethod
    async def handle(self, query: Q) -> R:
        """Execute a read-only query."""
