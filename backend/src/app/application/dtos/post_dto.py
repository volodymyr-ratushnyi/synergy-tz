from dataclasses import dataclass

from app.application.dtos.user_dto import UserDto
from app.domain.entities.post import Post
from app.domain.entities.user import User


@dataclass(frozen=True, slots=True)
class PostDto:
    external_id: int
    user_external_id: int
    title: str
    body: str
    views: int
    tags: list[str]
    reactions: dict[str, int]

    @classmethod
    def from_entity(cls, post: Post) -> "PostDto":
        return cls(
            external_id=post.external_id,
            user_external_id=post.user_external_id,
            title=post.title,
            body=post.body,
            views=post.views,
            tags=post.tags,
            reactions=post.reactions,
        )


@dataclass(frozen=True, slots=True)
class PostDetailDto:
    external_id: int
    user_external_id: int
    title: str
    body: str
    views: int
    tags: list[str]
    reactions: dict[str, int]
    author: UserDto

    @classmethod
    def from_entity(cls, post: Post, author: User) -> "PostDetailDto":
        return cls(
            external_id=post.external_id,
            user_external_id=post.user_external_id,
            title=post.title,
            body=post.body,
            views=post.views,
            tags=post.tags,
            reactions=post.reactions,
            author=UserDto.from_entity(author),
        )
