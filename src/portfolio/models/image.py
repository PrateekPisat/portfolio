from datetime import datetime

from sqlalchemy import Column, types
from sqlalchemy.orm import Mapped

from portfolio.models import Base


class Image(Base):
    __tablename__ = "image"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[int] = Column(types.Integer(), primary_key=True, autoincrement=True)
    width: Mapped[int] = Column(types.Integer(), nullable=False)
    height: Mapped[int] = Column(types.Integer(), nullable=False)
    blur_hash: Mapped[str] = Column(types.String(), nullable=False)
    description: Mapped[str] = Column(types.String(), nullable=True)
    city: Mapped[str] = Column(types.String(), nullable=True)
    country: Mapped[str] = Column(types.String(), nullable=True)
    full_path: Mapped[str] = Column(types.String(), nullable=False)
    thumbnail_path: Mapped[str] = Column(types.String(), nullable=False)
    created_at: Mapped[datetime] = Column(
        types.DateTime(timezone=True), nullable=False, default=datetime.now()
    )
    updated_at: Mapped[datetime] = Column(types.DateTime(timezone=True), nullable=True)
