from dataclasses import dataclass

from app.application.dtos.pagination import PaginatedResultDto, PaginationParams
from app.application.dtos.post_dto import PostDetailDto, PostDto
from app.application.interfaces.unit_of_work import UnitOfWork
from app.domain.entities.post import Post
from app.domain.exceptions import NotFoundError


@dataclass(frozen=True, slots=True)
class CreatePostData:
    user_external_id: int
    title: str
    body: str
    views: int = 0
    tags: list[str] | None = None
    reactions: dict[str, int] | None = None


@dataclass(frozen=True, slots=True)
class UpdatePostData:
    user_external_id: int | None = None
    title: str | None = None
    body: str | None = None
    views: int | None = None
    tags: list[str] | None = None
    reactions: dict[str, int] | None = None


class PostService:
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def list_posts(
        self,
        params: PaginationParams,
        user_external_id: int | None = None,
    ) -> PaginatedResultDto[PostDto]:
        posts = await self._uow.posts.list(
            offset=params.offset,
            limit=params.limit,
            sort_by=params.sort_by,
            sort_order=params.sort_order,
            user_external_id=user_external_id,
        )
        total = await self._uow.posts.count(user_external_id=user_external_id)
        return PaginatedResultDto(
            items=[PostDto.from_entity(post) for post in posts],
            total=total,
            offset=params.offset,
            limit=params.limit,
        )

    async def get_post(self, external_id: int) -> PostDetailDto:
        post = await self._uow.posts.get_by_id(external_id)
        if post is None:
            raise NotFoundError(f"Post {external_id} not found")

        author = await self._uow.users.get_by_id(post.user_external_id)
        if author is None:
            raise NotFoundError(f"Author {post.user_external_id} not found")

        return PostDetailDto.from_entity(post, author)

    async def create_post(self, data: CreatePostData) -> PostDto:
        author = await self._uow.users.get_by_id(data.user_external_id)
        if author is None:
            raise NotFoundError(f"User {data.user_external_id} not found")

        external_id = await self._uow.posts.get_next_external_id()
        post = Post(
            external_id=external_id,
            user_external_id=data.user_external_id,
            title=data.title,
            body=data.body,
            views=data.views,
            tags=data.tags or [],
            reactions=data.reactions or {},
        )
        created = await self._uow.posts.create(post)
        return PostDto.from_entity(created)

    async def update_post(self, external_id: int, data: UpdatePostData) -> PostDto:
        existing = await self._uow.posts.get_by_id(external_id)
        if existing is None:
            raise NotFoundError(f"Post {external_id} not found")

        user_external_id = (
            data.user_external_id
            if data.user_external_id is not None
            else existing.user_external_id
        )
        if user_external_id != existing.user_external_id:
            author = await self._uow.users.get_by_id(user_external_id)
            if author is None:
                raise NotFoundError(f"User {user_external_id} not found")

        updated = Post(
            external_id=external_id,
            user_external_id=user_external_id,
            title=data.title if data.title is not None else existing.title,
            body=data.body if data.body is not None else existing.body,
            views=data.views if data.views is not None else existing.views,
            tags=data.tags if data.tags is not None else existing.tags,
            reactions=data.reactions if data.reactions is not None else existing.reactions,
        )
        result = await self._uow.posts.update(updated)
        assert result is not None
        return PostDto.from_entity(result)

    async def delete_post(self, external_id: int) -> None:
        deleted = await self._uow.posts.delete(external_id)
        if not deleted:
            raise NotFoundError(f"Post {external_id} not found")
