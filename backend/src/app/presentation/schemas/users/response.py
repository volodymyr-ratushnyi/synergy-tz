from pydantic import BaseModel

from app.application.dtos.user_dto import UserDetailDto, UserDto
from app.presentation.schemas.common import PaginatedResponse


class UserResponse(BaseModel):
    external_id: int
    first_name: str
    last_name: str
    email: str
    username: str
    image: str
    role: str

    @classmethod
    def from_dto(cls, dto: UserDto) -> "UserResponse":
        return cls(
            external_id=dto.external_id,
            first_name=dto.first_name,
            last_name=dto.last_name,
            email=dto.email,
            username=dto.username,
            image=dto.image,
            role=dto.role,
        )


class PostSummaryResponse(BaseModel):
    external_id: int
    title: str
    views: int


class UserDetailResponse(UserResponse):
    posts: list[PostSummaryResponse]

    @classmethod
    def from_dto(cls, dto: UserDetailDto) -> "UserDetailResponse":
        return cls(
            external_id=dto.external_id,
            first_name=dto.first_name,
            last_name=dto.last_name,
            email=dto.email,
            username=dto.username,
            image=dto.image,
            role=dto.role,
            posts=[
                PostSummaryResponse(
                    external_id=post.external_id,
                    title=post.title,
                    views=post.views,
                )
                for post in dto.posts
            ],
        )


class PaginatedUsersResponse(PaginatedResponse[UserResponse]):
    @classmethod
    def from_dto(cls, dto) -> "PaginatedUsersResponse":
        return cls(
            items=[UserResponse.from_dto(item) for item in dto.items],
            total=dto.total,
            offset=dto.offset,
            limit=dto.limit,
        )
