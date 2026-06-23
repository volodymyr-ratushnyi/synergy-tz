from fastapi import APIRouter, Depends, Query, Response, status

from app.application.dtos.pagination import PaginationParams
from app.application.services.post_service import CreatePostData, PostService, UpdatePostData
from app.core.dependencies import get_post_service
from app.presentation.schemas.posts.request import (
    CreatePostRequest,
    PostSortField,
    UpdatePostRequest,
)
from app.presentation.schemas.posts.response import (
    PaginatedPostsResponse,
    PostDetailResponse,
    PostResponse,
)

router = APIRouter()


@router.get("", response_model=PaginatedPostsResponse)
async def list_posts(
    offset: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    sort_by: PostSortField = Query(PostSortField.external_id),
    sort_order: str = Query("asc", pattern="^(asc|desc)$"),
    user_external_id: int | None = Query(None),
    service: PostService = Depends(get_post_service),
) -> PaginatedPostsResponse:
    params = PaginationParams(
        offset=offset,
        limit=limit,
        sort_by=sort_by.value,
        sort_order=sort_order,
    )
    result = await service.list_posts(params, user_external_id=user_external_id)
    return PaginatedPostsResponse.from_dto(result)


@router.get("/{external_id}", response_model=PostDetailResponse)
async def get_post(
    external_id: int,
    service: PostService = Depends(get_post_service),
) -> PostDetailResponse:
    result = await service.get_post(external_id)
    return PostDetailResponse.from_dto(result)


@router.post("", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
async def create_post(
    body: CreatePostRequest,
    service: PostService = Depends(get_post_service),
) -> PostResponse:
    data = CreatePostData(
        user_external_id=body.user_external_id,
        title=body.title,
        body=body.body,
        views=body.views,
        tags=body.tags,
        reactions=body.reactions,
    )
    result = await service.create_post(data)
    return PostResponse.from_dto(result)


@router.put("/{external_id}", response_model=PostResponse)
async def update_post(
    external_id: int,
    body: UpdatePostRequest,
    service: PostService = Depends(get_post_service),
) -> PostResponse:
    data = UpdatePostData(
        user_external_id=body.user_external_id,
        title=body.title,
        body=body.body,
        views=body.views,
        tags=body.tags,
        reactions=body.reactions,
    )
    result = await service.update_post(external_id, data)
    return PostResponse.from_dto(result)


@router.delete("/{external_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_post(
    external_id: int,
    service: PostService = Depends(get_post_service),
) -> Response:
    await service.delete_post(external_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
