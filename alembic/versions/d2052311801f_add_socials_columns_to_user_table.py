"""Add socials columns to user table.

Revision ID: d2052311801f
Revises: 3be74c05c2e0
Create Date: 2023-02-16 07:27:20.207687

"""
import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision = "d2052311801f"
down_revision = "3be74c05c2e0"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "user", sa.Column("github_username", sa.String(), nullable=True), schema="portfolio"
    )
    op.add_column(
        "user", sa.Column("unsplash_username", sa.String(), nullable=True), schema="portfolio"
    )
    op.add_column("user", sa.Column("email", sa.String(), nullable=True), schema="portfolio")
    op.add_column(
        "user", sa.Column("about_picture_path", sa.String(), nullable=True), schema="portfolio"
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("user", "about_picture_path", schema="portfolio")
    op.drop_column("user", "email", schema="portfolio")
    op.drop_column("user", "unsplash_username", schema="portfolio")
    op.drop_column("user", "github_username", schema="portfolio")
    # ### end Alembic commands ###