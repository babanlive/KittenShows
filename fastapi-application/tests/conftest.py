from collections.abc import AsyncGenerator

import pytest

from core.models import db_helper
from httpx import AsyncClient
from main import main_app
from sqlalchemy.ext.asyncio import AsyncSession


@pytest.fixture(scope='session')
def anyio_backend():
    return 'asyncio'


@pytest.fixture(scope='function')
async def async_client() -> AsyncGenerator[AsyncClient, None]:
    async with AsyncClient(app=main_app, base_url='http://testserver') as client:
        yield client


@pytest.fixture(scope='function')
async def session() -> AsyncGenerator[AsyncSession, None]:
    async with db_helper.session_getter() as session:
        yield session
