from sqlalchemy import ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import Mapped, mapped_column

from app.infrastructure.persistence.models.base import Base


class PostModel(Base):
    __tablename__ = "posts"

    external_id: Mapped[int] = mapped_column(primary_key=True)
    user_external_id: Mapped[int] = mapped_column(ForeignKey("users.external_id"))
    title: Mapped[str] = mapped_column(String(512))
    body: Mapped[str] = mapped_column(Text)
    views: Mapped[int] = mapped_column(Integer)
    tags: Mapped[list] = mapped_column(JSONB)
    reactions: Mapped[dict] = mapped_column(JSONB)
