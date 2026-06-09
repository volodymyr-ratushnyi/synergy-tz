from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class User:
    external_id: int
    first_name: str
    last_name: str
    email: str
    username: str
    image: str
    role: str
