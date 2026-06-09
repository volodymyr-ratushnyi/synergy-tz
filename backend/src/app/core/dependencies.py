from collections.abc import AsyncGenerator

from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.application.interfaces.unit_of_work import UnitOfWork
from app.application.services.post_service import PostService
from app.application.services.sync_service import SyncService
from app.application.services.user_service import UserService
from app.core.config import Settings, get_settings
from app.infrastructure.external.dummyjson_client import DummyJsonClient
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


def get_dummyjson_client(settings: Settings = Depends(get_settings)) -> DummyJsonClient:
    return DummyJsonClient(
        base_url=settings.dummyjson_base_url,
        timeout=settings.dummyjson_timeout_seconds,
    )


def get_sync_service(
    uow: UnitOfWork = Depends(get_uow),
    client: DummyJsonClient = Depends(get_dummyjson_client),
) -> SyncService:
    return SyncService(uow=uow, client=client)


def get_user_service(uow: UnitOfWork = Depends(get_uow)) -> UserService:
    return UserService(uow=uow)


def get_post_service(uow: UnitOfWork = Depends(get_uow)) -> PostService:
    return PostService(uow=uow)
