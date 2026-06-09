from sqlalchemy import delete, func, select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.persistence.mappers import to_user_entity
from app.infrastructure.persistence.models.user_model import UserModel

USER_SORT_FIELDS = {
    "external_id": UserModel.external_id,
    "first_name": UserModel.first_name,
    "last_name": UserModel.last_name,
    "email": UserModel.email,
    "username": UserModel.username,
    "role": UserModel.role,
}


class SqlAlchemyUserRepository(UserRepository):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session

    async def upsert_many(self, users: list[User]) -> int:
        if not users:
            return 0

        values = [
            {
                "external_id": user.external_id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "username": user.username,
                "image": user.image,
                "role": user.role,
            }
            for user in users
        ]

        stmt = insert(UserModel).values(values)
        stmt = stmt.on_conflict_do_update(
            index_elements=["external_id"],
            set_={
                "first_name": stmt.excluded.first_name,
                "last_name": stmt.excluded.last_name,
                "email": stmt.excluded.email,
                "username": stmt.excluded.username,
                "image": stmt.excluded.image,
                "role": stmt.excluded.role,
            },
        )
        await self._session.execute(stmt)
        return len(users)

    async def get_by_id(self, external_id: int) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.external_id == external_id)
        )
        model = result.scalar_one_or_none()
        return to_user_entity(model) if model else None

    async def list(
        self,
        *,
        offset: int,
        limit: int,
        sort_by: str,
        sort_order: str,
    ) -> list[User]:
        sort_column = USER_SORT_FIELDS.get(sort_by, UserModel.external_id)
        order = sort_column.asc() if sort_order == "asc" else sort_column.desc()

        result = await self._session.execute(
            select(UserModel).order_by(order).offset(offset).limit(limit)
        )
        return [to_user_entity(model) for model in result.scalars().all()]

    async def count(self) -> int:
        result = await self._session.execute(select(func.count()).select_from(UserModel))
        return result.scalar_one()

    async def get_next_external_id(self) -> int:
        result = await self._session.execute(select(func.max(UserModel.external_id)))
        max_id = result.scalar_one_or_none()
        return (max_id or 0) + 1

    async def create(self, user: User) -> User:
        model = UserModel(
            external_id=user.external_id,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            username=user.username,
            image=user.image,
            role=user.role,
        )
        self._session.add(model)
        await self._session.flush()
        return to_user_entity(model)

    async def update(self, user: User) -> User | None:
        result = await self._session.execute(
            select(UserModel).where(UserModel.external_id == user.external_id)
        )
        model = result.scalar_one_or_none()
        if model is None:
            return None

        model.first_name = user.first_name
        model.last_name = user.last_name
        model.email = user.email
        model.username = user.username
        model.image = user.image
        model.role = user.role
        await self._session.flush()
        return to_user_entity(model)

    async def delete(self, external_id: int) -> bool:
        result = await self._session.execute(
            delete(UserModel).where(UserModel.external_id == external_id)
        )
        return result.rowcount > 0
