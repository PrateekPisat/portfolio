"""Update image path column names.

Revision ID: 800822ad54e2
Revises: ad221fafd493
Create Date: 2023-02-05 12:52:54.437165

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "800822ad54e2"
down_revision = "ad221fafd493"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("image", sa.Column("full_path", sa.String(), nullable=False), schema="portfolio")
    op.add_column(
        "image", sa.Column("thumbnail_path", sa.String(), nullable=False), schema="portfolio"
    )
    op.drop_column("image", "thumbnail_s3_url", schema="portfolio")
    op.drop_column("image", "full_s3_url", schema="portfolio")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "image",
        sa.Column("full_s3_url", sa.VARCHAR(), autoincrement=False, nullable=False),
        schema="portfolio",
    )
    op.add_column(
        "image",
        sa.Column("thumbnail_s3_url", sa.VARCHAR(), autoincrement=False, nullable=False),
        schema="portfolio",
    )
    op.drop_column("image", "thumbnail_path", schema="portfolio")
    op.drop_column("image", "full_path", schema="portfolio")
    # ### end Alembic commands ###
