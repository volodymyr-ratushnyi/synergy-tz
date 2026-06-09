from dataclasses import dataclass
from typing import Generic, TypeVar

T = TypeVar("T")


@dataclass(frozen=True, slots=True)
class PaginationParams:
    offset: int
    limit: int
    sort_by: str
    sort_order: str


@dataclass(frozen=True, slots=True)
class PaginatedResultDto(Generic[T]):
    items: list[T]
    total: int
    offset: int
    limit: int
