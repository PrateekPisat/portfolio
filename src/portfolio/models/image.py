from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, ForeignKey, types
from sqlalchemy.orm import Mapped, relationship

from portfolio.models import Base


class Image(Base):
    __tablename__ = "image"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[int] = Column(types.Integer(), primary_key=True, autoincrement=True)
    group_id: Mapped[int] = Column(ForeignKey("portfolio.group.id"), nullable=True)

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

    group: Mapped[Group] = relationship("Group", lazy="selectin")


class Group(Base):
    __tablename__ = "group"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[int] = Column(types.Integer(), primary_key=True, autoincrement=True)
    name: Mapped[str] = Column(types.String(), nullable=False)

    created_at: Mapped[datetime] = Column(
        types.DateTime(timezone=True), nullable=False, default=datetime.now()
    )
    updated_at: Mapped[datetime] = Column(types.DateTime(timezone=True), nullable=True)
