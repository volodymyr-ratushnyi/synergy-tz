from pydantic import BaseModel, Field


class CreateUserRequest(BaseModel):
    first_name: str = Field(min_length=1, max_length=255)
    last_name: str = Field(min_length=1, max_length=255)
    email: str = Field(min_length=1, max_length=255)
    username: str = Field(min_length=1, max_length=255)
    image: str = Field(default="", max_length=512)
    role: str = Field(default="user", max_length=50)


class UpdateUserRequest(BaseModel):
    first_name: str | None = Field(default=None, min_length=1, max_length=255)
    last_name: str | None = Field(default=None, min_length=1, max_length=255)
    email: str | None = Field(default=None, min_length=1, max_length=255)
    username: str | None = Field(default=None, min_length=1, max_length=255)
    image: str | None = Field(default=None, max_length=512)
    role: str | None = Field(default=None, max_length=50)
