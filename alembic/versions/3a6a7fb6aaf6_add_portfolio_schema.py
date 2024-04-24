"""Add portfolio schema.

Revision ID: 3a6a7fb6aaf6
Revises:
Create Date: 2022-12-07 19:08:46.992692

"""

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "3a6a7fb6aaf6"
down_revision = None
branch_labels = None
depends_on = None

schema = "portfolio"


def upgrade() -> None:
    op.execute(f"CREATE SCHEMA {schema};")


def downgrade() -> None:
    op.execute(f"DROP SCHEMA {schema};")
