from pydantic import BaseModel, Field


class CreatePostRequest(BaseModel):
    user_external_id: int
    title: str = Field(min_length=1, max_length=512)
    body: str = Field(min_length=1)
    views: int = Field(default=0, ge=0)
    tags: list[str] = Field(default_factory=list)
    reactions: dict[str, int] = Field(default_factory=dict)


class UpdatePostRequest(BaseModel):
    user_external_id: int | None = None
    title: str | None = Field(default=None, min_length=1, max_length=512)
    body: str | None = Field(default=None, min_length=1)
    views: int | None = Field(default=None, ge=0)
    tags: list[str] | None = None
    reactions: dict[str, int] | None = None
