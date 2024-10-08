from core.models import db_helper
from core.schemas.kittens import KittenCreate, KittenRead
from crud import kittens as crud_kittens
from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=['Kittens'])


@router.get('', response_model=list[KittenRead])
async def get_kittens(
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
    name: str | None = Query(None),
    breed_id: float | None = Query(None),
    min_age: float | None = Query(None),
    max_age: float | None = Query(None),
) -> list[KittenRead]:
    return await crud_kittens.get_filtered_kittens(
        session, name=name, breed_id=breed_id, min_age=min_age, max_age=max_age
    )



@router.post('', response_model=KittenRead)
async def create_kitten(
    kitten_create: KittenCreate,
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
):
    return await crud_kittens.create_kitten(session=session, kitten_create=kitten_create)


@router.put('/{kitten_id}', response_model=KittenRead)
async def update_kitten(
    kitten_id: int,
    kitten_update: KittenCreate,
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
):
    return await crud_kittens.update_kitten(session=session, kitten_id=kitten_id, kitten_update=kitten_update)


@router.delete('/{kitten_id}')
async def delete_kitten(
    kitten_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
):
    await crud_kittens.delete_kitten(session=session, kitten_id=kitten_id)
    return {'message': 'Kitten deleted successfully'}
