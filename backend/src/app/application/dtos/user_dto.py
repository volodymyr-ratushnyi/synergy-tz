from dataclasses import dataclass

from app.domain.entities.post import Post
from app.domain.entities.user import User


@dataclass(frozen=True, slots=True)
class UserDto:
    external_id: int
    first_name: str
    last_name: str
    email: str
    username: str
    image: str
    role: str

    @classmethod
    def from_entity(cls, user: User) -> "UserDto":
        return cls(
            external_id=user.external_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=user.username,
            image=user.image,
            role=user.role,
        )


@dataclass(frozen=True, slots=True)
class UserDetailDto:
    external_id: int
    first_name: str
    last_name: str
    email: str
    username: str
    image: str
    role: str
    posts: list["PostSummaryDto"]

    @classmethod
    def from_entity(cls, user: User, posts: list[Post]) -> "UserDetailDto":
        return cls(
            external_id=user.external_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=user.username,
            image=user.image,
            role=user.role,
            posts=[PostSummaryDto.from_entity(post) for post in posts],
        )


@dataclass(frozen=True, slots=True)
class PostSummaryDto:
    external_id: int
    title: str
    views: int

    @classmethod
    def from_entity(cls, post: Post) -> "PostSummaryDto":
        return cls(
            external_id=post.external_id,
            title=post.title,
            views=post.views,
        )
