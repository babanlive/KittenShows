# core/models/models.py
from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Breed(Base):
    __tablename__ = 'breeds'

    name: Mapped[str] = mapped_column(String, nullable=False, index=True)

    kittens: Mapped[list['Kitten']] = relationship('Kitten', back_populates='breed')


class Kitten(Base):
    __tablename__ = 'kittens'

    name: Mapped[str] = mapped_column(String, nullable=False)
    color: Mapped[str] = mapped_column(String, nullable=False)
    age: Mapped[int] = mapped_column(Integer, nullable=False)  # Age in months
    description: Mapped[str] = mapped_column(String, nullable=True)

    breed_id: Mapped[int] = mapped_column(ForeignKey('breeds.id'), nullable=False)

    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now(), nullable=False
    )

    breed: Mapped['Breed'] = relationship('Breed', back_populates='kittens')
