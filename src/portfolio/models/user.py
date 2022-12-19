from datetime import datetime

from sqlalchemy import Column, types
from sqlalchemy.orm import Mapped

from portfolio.models import Base


class User(Base):
    __tablename__ = "user"
    __table_args__ = {"schema": "portfolio"}

    id: Mapped[int] = Column(types.Integer(), primary_key=True, autoincrement=True)
    username: Mapped[str] = Column(types.String(), nullable=False)
    password: Mapped[str] = Column(types.String(), nullable=False)
    first_name: Mapped[str] = Column(types.String(), nullable=False)
    last_name: Mapped[str] = Column(types.String(), nullable=False)
    instagram_username: Mapped[str] = Column(types.String(), nullable=False)
    bio: Mapped[str] = Column(types.String(), nullable=False)
    location: Mapped[str] = Column(types.String(), nullable=False)
    total_photos: Mapped[int] = Column(types.Integer(), nullable=False)
    created_at: Mapped[datetime] = Column(
        types.DateTime(timezone=True), nullable=False, default=datetime.now()
    )
    updated_at: Mapped[datetime] = Column(types.DateTime(timezone=True), nullable=True)
