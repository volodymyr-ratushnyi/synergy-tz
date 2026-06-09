from fastapi import APIRouter

from app.presentation.api.v1.endpoints import health, sync

api_router = APIRouter()
api_router.include_router(health.router, tags=["health"])
api_router.include_router(sync.router, tags=["sync"])
