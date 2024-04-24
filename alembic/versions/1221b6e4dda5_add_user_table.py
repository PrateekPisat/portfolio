"""Add user table.

Revision ID: 1221b6e4dda5
Revises: 5e308f9c6e75
Create Date: 2022-12-23 11:38:48.502187

"""

import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "1221b6e4dda5"
down_revision = "5e308f9c6e75"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "user",
        sa.Column("id", sa.Integer(), autoincrement=True, nullable=False),
        sa.Column("username", sa.String(), nullable=False),
        sa.Column("password", sa.String(), nullable=False),
        sa.Column("first_name", sa.String(), nullable=False),
        sa.Column("last_name", sa.String(), nullable=False),
        sa.Column("instagram_username", sa.String(), nullable=False),
        sa.Column("bio", sa.String(), nullable=False),
        sa.Column("location", sa.String(), nullable=False),
        sa.Column("total_photos", sa.Integer(), nullable=False),
        sa.Column("created_at", sa.DateTime(timezone=True), nullable=False),
        sa.Column("updated_at", sa.DateTime(timezone=True), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        schema="portfolio",
    )
    op.alter_column(
        "image",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=True,
        schema="portfolio",
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "image",
        "updated_at",
        existing_type=postgresql.TIMESTAMP(timezone=True),
        nullable=False,
        schema="portfolio",
    )
    op.drop_table("user", schema="portfolio")
    # ### end Alembic commands ###
