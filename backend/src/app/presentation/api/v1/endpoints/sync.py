from fastapi import APIRouter, Depends

from app.application.services.sync_service import SyncService
from app.core.dependencies import get_sync_service
from app.presentation.schemas.sync.response import SyncResponse

router = APIRouter()


@router.get("/sync", response_model=SyncResponse)
async def sync_data(
    service: SyncService = Depends(get_sync_service),
) -> SyncResponse:
    result = await service.sync()
    return SyncResponse.from_dto(result)
