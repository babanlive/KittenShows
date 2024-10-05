from collections.abc import Sequence

from core.models import Breed
from core.schemas.breeds import BreedCreate, BreedUpdate
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_all_breeds(session: AsyncSession) -> Sequence[Breed]:
    stmt = select(Breed).order_by(Breed.id)
    result = await session.scalars(stmt)
    return result.all()


async def create_breed(session: AsyncSession, breed_create: BreedCreate) -> Breed:
    stmt = select(Breed).where(Breed.name == breed_create.name)
    result = await session.execute(stmt)
    existing_breed = result.scalar()
    if existing_breed:
        raise HTTPException(status_code=400, detail='Breed already exists')

    breed = Breed(**breed_create.model_dump())
    session.add(breed)
    await session.commit()
    await session.refresh(breed)
    return breed


async def update_breed(session: AsyncSession, breed_id: int, breed_update: BreedUpdate) -> Breed:
    stmt = select(Breed).where(Breed.id == breed_id)
    result = await session.scalars(stmt)
    breed = result.first()
    if not breed:
        raise HTTPException(status_code=404, detail='Breed not found')

    for key, value in breed_update.model_dump().items():
        setattr(breed, key, value)

    await session.commit()
    await session.refresh(breed)
    return breed


async def delete_breed(session: AsyncSession, breed_id: int) -> None:
    breed = await session.get(Breed, breed_id)
    if not breed:
        raise HTTPException(status_code=404, detail='Breed not found')

    await session.delete(breed)
    await session.commit()
