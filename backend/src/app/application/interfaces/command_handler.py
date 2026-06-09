from abc import ABC, abstractmethod
from typing import TypeVar

C = TypeVar("C")
R = TypeVar("R")


class CommandHandler[C, R](ABC):
    @abstractmethod
    async def handle(self, command: C) -> R:
        """Execute a command that mutates application state."""
