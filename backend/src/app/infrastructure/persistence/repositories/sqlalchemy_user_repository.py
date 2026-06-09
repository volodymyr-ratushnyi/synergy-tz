from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.entities.user import User
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.persistence.models.user_model import UserModel


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
