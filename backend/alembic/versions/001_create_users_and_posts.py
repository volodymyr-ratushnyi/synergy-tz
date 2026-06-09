"""create users and posts tables

Revision ID: 001
Revises:
Create Date: 2026-06-09

"""

from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import postgresql

revision: str = "001"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "users",
        sa.Column("external_id", sa.Integer(), nullable=False),
        sa.Column("first_name", sa.String(length=255), nullable=False),
        sa.Column("last_name", sa.String(length=255), nullable=False),
        sa.Column("email", sa.String(length=255), nullable=False),
        sa.Column("username", sa.String(length=255), nullable=False),
        sa.Column("image", sa.String(length=512), nullable=False),
        sa.Column("role", sa.String(length=50), nullable=False),
        sa.PrimaryKeyConstraint("external_id"),
    )
    op.create_table(
        "posts",
        sa.Column("external_id", sa.Integer(), nullable=False),
        sa.Column("user_external_id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(length=512), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("views", sa.Integer(), nullable=False),
        sa.Column("tags", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.Column("reactions", postgresql.JSONB(astext_type=sa.Text()), nullable=False),
        sa.ForeignKeyConstraint(["user_external_id"], ["users.external_id"]),
        sa.PrimaryKeyConstraint("external_id"),
    )


def downgrade() -> None:
    op.drop_table("posts")
    op.drop_table("users")
