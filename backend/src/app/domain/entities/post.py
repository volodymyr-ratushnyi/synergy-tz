from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Post:
    external_id: int
    user_external_id: int
    title: str
    body: str
    views: int
    tags: list[str]
    reactions: dict[str, int]
