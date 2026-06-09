from pydantic import BaseModel

from app.application.dtos.sync_result_dto import SyncResultDto


class SyncResponse(BaseModel):
    users_count: int
    posts_count: int

    @classmethod
    def from_dto(cls, dto: SyncResultDto) -> "SyncResponse":
        return cls(users_count=dto.users_count, posts_count=dto.posts_count)
