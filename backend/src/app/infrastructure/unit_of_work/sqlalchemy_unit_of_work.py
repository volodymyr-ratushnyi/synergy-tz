from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.unit_of_work import UnitOfWork
from app.domain.repositories.post_repository import PostRepository
from app.domain.repositories.user_repository import UserRepository
from app.infrastructure.persistence.repositories.sqlalchemy_post_repository import (
    SqlAlchemyPostRepository,
)
from app.infrastructure.persistence.repositories.sqlalchemy_user_repository import (
    SqlAlchemyUserRepository,
)


class SqlAlchemyUnitOfWork(UnitOfWork):
    def __init__(self, session: AsyncSession) -> None:
        self._session = session
        self._users: UserRepository | None = None
        self._posts: PostRepository | None = None

    @property
    def users(self) -> UserRepository:
        if self._users is None:
            self._users = SqlAlchemyUserRepository(self._session)
        return self._users

    @property
    def posts(self) -> PostRepository:
        if self._posts is None:
            self._posts = SqlAlchemyPostRepository(self._session)
        return self._posts

    async def commit(self) -> None:
        await self._session.commit()

    async def rollback(self) -> None:
        await self._session.rollback()
