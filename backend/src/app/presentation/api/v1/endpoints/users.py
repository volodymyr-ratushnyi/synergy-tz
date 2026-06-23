from fastapi import APIRouter, Depends, Query, Response, status

from app.application.dtos.pagination import PaginationParams
from app.application.services.user_service import CreateUserData, UpdateUserData, UserService
from app.core.dependencies import get_user_service
from app.presentation.schemas.users.request import (
    CreateUserRequest,
    UpdateUserRequest,
    UserSortField,
)
from app.presentation.schemas.users.response import (
    PaginatedUsersResponse,
    UserDetailResponse,
    UserResponse,
)

router = APIRouter()


@router.get("", response_model=PaginatedUsersResponse)
async def list_users(
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    sort_by: UserSortField = Query(UserSortField.external_id),
    sort_order: str = Query("asc", pattern="^(asc|desc)$"),
    service: UserService = Depends(get_user_service),
) -> PaginatedUsersResponse:
    params = PaginationParams(
        offset=offset,
        limit=limit,
        sort_by=sort_by.value,
        sort_order=sort_order,
    )
    result = await service.list_users(params)
    return PaginatedUsersResponse.from_dto(result)


@router.get("/{external_id}", response_model=UserDetailResponse)
async def get_user(
    external_id: int,
    service: UserService = Depends(get_user_service),
) -> UserDetailResponse:
    result = await service.get_user(external_id)
    return UserDetailResponse.from_dto(result)


@router.post("", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
async def create_user(
    body: CreateUserRequest,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    data = CreateUserData(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        username=body.username,
        image=body.image,
        role=body.role,
    )
    result = await service.create_user(data)
    return UserResponse.from_dto(result)


@router.put("/{external_id}", response_model=UserResponse)
async def update_user(
    external_id: int,
    body: UpdateUserRequest,
    service: UserService = Depends(get_user_service),
) -> UserResponse:
    data = UpdateUserData(
        first_name=body.first_name,
        last_name=body.last_name,
        email=body.email,
        username=body.username,
        image=body.image,
        role=body.role,
    )
    result = await service.update_user(external_id, data)
    return UserResponse.from_dto(result)


@router.delete("/{external_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_user(
    external_id: int,
    service: UserService = Depends(get_user_service),
) -> Response:
    await service.delete_user(external_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
