from pydantic import BaseModel

from app.application.dtos.post_dto import PostDetailDto, PostDto
from app.presentation.schemas.common import PaginatedResponse
from app.presentation.schemas.users.response import UserResponse


class PostResponse(BaseModel):
    external_id: int
    user_external_id: int
    title: str
    body: str
    views: int
    tags: list[str]
    reactions: dict[str, int]

    @classmethod
    def from_dto(cls, dto: PostDto) -> "PostResponse":
        return cls(
            external_id=dto.external_id,
            user_external_id=dto.user_external_id,
            title=dto.title,
            body=dto.body,
            views=dto.views,
            tags=dto.tags,
            reactions=dto.reactions,
        )


class PostDetailResponse(PostResponse):
    author: UserResponse

    @classmethod
    def from_dto(cls, dto: PostDetailDto) -> "PostDetailResponse":
        return cls(
            external_id=dto.external_id,
            user_external_id=dto.user_external_id,
            title=dto.title,
            body=dto.body,
            views=dto.views,
            tags=dto.tags,
            reactions=dto.reactions,
            author=UserResponse.from_dto(dto.author),
        )


class PaginatedPostsResponse(PaginatedResponse[PostResponse]):
    @classmethod
    def from_dto(cls, dto) -> "PaginatedPostsResponse":
        return cls(
            items=[PostResponse.from_dto(item) for item in dto.items],
            total=dto.total,
            offset=dto.offset,
            limit=dto.limit,
        )
