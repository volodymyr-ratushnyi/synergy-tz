from dataclasses import dataclass

from app.application.dtos.pagination import PaginatedResultDto, PaginationParams
from app.application.dtos.user_dto import UserDetailDto, UserDto
from app.application.interfaces.unit_of_work import UnitOfWork
from app.domain.entities.user import User
from app.domain.exceptions import NotFoundError


@dataclass(frozen=True, slots=True)
class CreateUserData:
    first_name: str
    last_name: str
    email: str
    username: str
    image: str
    role: str


@dataclass(frozen=True, slots=True)
class UpdateUserData:
    first_name: str | None = None
    last_name: str | None = None
    email: str | None = None
    username: str | None = None
    image: str | None = None
    role: str | None = None


class UserService:
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def list_users(self, params: PaginationParams) -> PaginatedResultDto[UserDto]:
        users = await self._uow.users.list(
            offset=params.offset,
            limit=params.limit,
            sort_by=params.sort_by,
            sort_order=params.sort_order,
        )
        total = await self._uow.users.count()
        return PaginatedResultDto(
            items=[UserDto.from_entity(user) for user in users],
            total=total,
            offset=params.offset,
            limit=params.limit,
        )

    async def get_user(self, external_id: int) -> UserDetailDto:
        user = await self._uow.users.get_by_id(external_id)
        if user is None:
            raise NotFoundError(f"User {external_id} not found")

        posts = await self._uow.posts.list_by_user(external_id)
        return UserDetailDto.from_entity(user, posts)

    async def create_user(self, data: CreateUserData) -> UserDto:
        external_id = await self._uow.users.get_next_external_id()
        user = User(
            external_id=external_id,
            first_name=data.first_name,
            last_name=data.last_name,
            email=data.email,
            username=data.username,
            image=data.image,
            role=data.role,
        )
        created = await self._uow.users.create(user)
        return UserDto.from_entity(created)

    async def update_user(self, external_id: int, data: UpdateUserData) -> UserDto:
        existing = await self._uow.users.get_by_id(external_id)
        if existing is None:
            raise NotFoundError(f"User {external_id} not found")

        updated = User(
            external_id=external_id,
            first_name=data.first_name if data.first_name is not None else existing.first_name,
            last_name=data.last_name if data.last_name is not None else existing.last_name,
            email=data.email if data.email is not None else existing.email,
            username=data.username if data.username is not None else existing.username,
            image=data.image if data.image is not None else existing.image,
            role=data.role if data.role is not None else existing.role,
        )
        result = await self._uow.users.update(updated)
        assert result is not None
        return UserDto.from_entity(result)

    async def delete_user(self, external_id: int) -> None:
        existing = await self._uow.users.get_by_id(external_id)
        if existing is None:
            raise NotFoundError(f"User {external_id} not found")

        await self._uow.posts.delete_by_user(external_id)
        await self._uow.users.delete(external_id)
