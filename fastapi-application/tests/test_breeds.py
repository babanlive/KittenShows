import pytest

from httpx import AsyncClient


@pytest.mark.anyio
async def test_create_breed(async_client: AsyncClient):
    response = await async_client.post('/api/v1/breeds', json={'name': 'Maine Coon'})
    assert response.status_code == 200
    assert response.json()['name'] == 'Maine Coon'


@pytest.mark.anyio
async def test_get_breeds(async_client: AsyncClient):
    response = await async_client.get('/api/v1/breeds')
    assert response.status_code == 200
    breeds = response.json()
    assert len(breeds) > 0


@pytest.mark.anyio
async def test_update_breed(async_client: AsyncClient):
    response = await async_client.post('/api/v1/breeds', json={'name': 'Maine Coon'})
    breed_id = response.json()['id']

    updated_response = await async_client.put(f'/api/v1/breeds/{breed_id}', json={'name': 'Siberian'})
    assert updated_response.status_code == 200
    assert updated_response.json()['name'] == 'Siberian'


@pytest.mark.anyio
async def test_delete_breed(async_client: AsyncClient):
    response = await async_client.post('/api/v1/breeds', json={'dname': 'Maine Coon'})
    breed_id = response.json()['id']

    delete_response = await async_client.delete(f'/api/v1/breeds/{breed_id}')
    assert delete_response.status_code == 200
    assert delete_response.json()['message'] == 'Breed deleted successfully'
