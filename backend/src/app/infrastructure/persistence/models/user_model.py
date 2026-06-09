from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base


class UserModel(Base):
    __tablename__ = "users"

    external_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(255))
    last_name: Mapped[str] = mapped_column(String(255))
    email: Mapped[str] = mapped_column(String(255))
    username: Mapped[str] = mapped_column(String(255))
    image: Mapped[str] = mapped_column(String(512))
    role: Mapped[str] = mapped_column(String(50))
