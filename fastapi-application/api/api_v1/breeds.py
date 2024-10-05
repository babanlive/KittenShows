from core.models import db_helper
from core.schemas.breeds import BreedCreate, BreedRead
from crud import breeds as crud_breeds
from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession


router = APIRouter(tags=['Breeds'])


@router.get('', response_model=list[BreedRead])
async def get_breeds(session: AsyncSession = Depends(db_helper.session_getter)):  # noqa: B008
    return await crud_breeds.get_breeds(session=session)


@router.post('', response_model=BreedRead)
async def create_breed(
    breed_create: BreedCreate,
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
):
    return await crud_breeds.create_breed(session=session, breed_create=breed_create)


@router.put('/{breed_id}', response_model=BreedRead)
async def update_breed(
    breed_id: int,
    breed_update: BreedCreate,
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
):
    return await crud_breeds.update_breed(
        session=session, breed_id=breed_id, breed_update=breed_update
    )


@router.delete('/{breed_id}')
async def delete_breed(
    breed_id: int,
    session: AsyncSession = Depends(db_helper.session_getter),  # noqa: B008
):
    await crud_breeds.delete_breed(session=session, breed_id=breed_id)
    return {'message': 'Breed deleted successfully'}
