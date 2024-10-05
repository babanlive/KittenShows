from collections.abc import Sequence

from core.models import Breed, Kitten
from core.schemas.kittens import KittenCreate, KittenUpdate
from fastapi import HTTPException
from sqlalchemy import and_, select
from sqlalchemy.ext.asyncio import AsyncSession


async def get_filtered_kittens(
    session: AsyncSession, name: str = None, breed_id: int = None, min_age: int = None, max_age: int = None
) -> Sequence[Kitten]:
    filters = []
    if name:
        filters.append(Kitten.name.ilike(f'%{name}%'))
    if breed_id:
        filters.append(Kitten.breed_id == breed_id)
    if min_age is not None:
        filters.append(Kitten.age >= min_age)
    if max_age is not None:
        filters.append(Kitten.age <= max_age)

    stmt = select(Kitten).where(and_(*filters)).order_by(Kitten.id)
    result = await session.scalars(stmt)
    return result.all()


async def get_kitten_by_id(session: AsyncSession, kitten_id: int) -> Kitten | None:
    stmt = select(Kitten).where(Kitten.id == kitten_id)
    result = await session.scalars(stmt)
    return result.first()


async def create_kitten(session: AsyncSession, kitten_create: KittenCreate) -> Kitten:
    kitten_name = kitten_create.name
    breed_id = kitten_create.breed_id

    breed = await session.get(Breed, breed_id)
    if not breed:
        raise HTTPException(status_code=400, detail=f'Breed with id {breed_id} does not exist')

    stmt = select(Kitten).filter(Kitten.name == kitten_name, Kitten.breed_id == breed_id)
    result = await session.execute(stmt)
    existing_kitten = result.scalar()

    if existing_kitten:
        raise HTTPException(status_code=400, detail='Kitten already exists in this breed')

    kitten = Kitten(**kitten_create.model_dump())
    session.add(kitten)
    await session.commit()
    await session.refresh(kitten)
    return kitten


async def update_kitten(session: AsyncSession, kitten_id: int, kitten_update: KittenUpdate) -> Kitten:
    # Получение котенка
    stmt = select(Kitten).where(Kitten.id == kitten_id)
    result = await session.scalars(stmt)
    kitten = result.first()

    if not kitten:
        raise HTTPException(status_code=404, detail='Kitten not found')

    breed_id = kitten_update.breed_id
    breed_stmt = select(Breed).where(Breed.id == breed_id)
    breed_result = await session.scalars(breed_stmt)
    breed = breed_result.first()

    if not breed:
        raise HTTPException(status_code=400, detail=f'Breed with id {breed_id} does not exist')

    for key, value in kitten_update.model_dump().items():
        setattr(kitten, key, value)

    await session.commit()
    await session.refresh(kitten)
    return kitten


async def delete_kitten(session: AsyncSession, kitten_id: int) -> None:
    kitten = await get_kitten_by_id(session=session, kitten_id=kitten_id)

    if kitten:
        await session.delete(kitten)
        await session.commit()
