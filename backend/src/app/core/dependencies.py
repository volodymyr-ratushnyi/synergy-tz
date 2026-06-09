from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.unit_of_work import UnitOfWork
from app.infrastructure.persistence.database import get_session
from app.infrastructure.unit_of_work.sqlalchemy_unit_of_work import SqlAlchemyUnitOfWork


async def get_uow(
    session: AsyncSession = Depends(get_session),
) -> AsyncGenerator[UnitOfWork, None]:
    uow = SqlAlchemyUnitOfWork(session)
    try:
        yield uow
        await uow.commit()
    except Exception:
        await uow.rollback()
        raise
