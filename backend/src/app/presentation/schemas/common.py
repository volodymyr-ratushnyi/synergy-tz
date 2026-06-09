from typing import Generic, TypeVar

from pydantic import BaseModel, Field

from app.application.dtos.pagination import PaginatedResultDto

T = TypeVar("T")


class PaginationQuery(BaseModel):
    offset: int = Field(default=0, ge=0)
    limit: int = Field(default=20, ge=1, le=100)
    sort_by: str = "external_id"
    sort_order: str = Field(default="asc", pattern="^(asc|desc)$")


class PaginatedResponse(BaseModel, Generic[T]):
    items: list[T]
    total: int
    offset: int
    limit: int

    @classmethod
    def from_dto(cls, dto: PaginatedResultDto) -> "PaginatedResponse":
        return cls(
            items=dto.items,
            total=dto.total,
            offset=dto.offset,
            limit=dto.limit,
        )
