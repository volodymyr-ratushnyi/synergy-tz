from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class SyncResultDto:
    users_count: int
    posts_count: int
