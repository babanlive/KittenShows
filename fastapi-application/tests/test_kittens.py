import pytest

from httpx import AsyncClient


@pytest.mark.anyio
async def test_create_kitten(async_client: AsyncClient):
    breed_response = await async_client.post('/api/v1/breeds', json={'name': 'Siberian'})
    breed_id = breed_response.json()['id']

    data = {
        'name': 'Pushok',
        'color': 'grey',
        'age': 4,
        'description': 'Active',
        'breed_id': breed_id,
    }
    response = await async_client.post('/api/v1/kittens', json=data)
    assert response.status_code == 200
    assert response.json()['name'] == 'Pushok'
    assert response.json()['color'] == 'grey'


@pytest.mark.anyio
async def test_get_kittens(async_client: AsyncClient):
    response = await async_client.get('/api/v1/kittens')
    assert response.status_code == 200
    kittens = response.json()
    assert len(kittens) > 0


@pytest.mark.anyio
async def test_update_kitten(async_client: AsyncClient):
    breed_response = await async_client.post('/api/v1/breeds', json={'name': 'Maine Coon'})
    breed_id = breed_response.json()['id']

    data = {
        'name': 'Snow',
        'color': 'white',
        'age': 2,
        'description': 'Сurious',
        'breed_id': breed_id,
    }
    create_response = await async_client.post('/api/v1/kittens', json=data)
    kitten_id = create_response.json()['id']

    updated_data = {
        'name': 'Pushok',
        'color': 'grey',
        'age': 3,
        'description': 'Active',
        'breed_id': breed_id,
    }
    response = await async_client.put(f'/api/v1/kittens/{kitten_id}', json=updated_data)
    assert response.status_code == 200
    assert response.json()['name'] == 'Pushok'
    assert response.json()['age'] == 3


@pytest.mark.anyio
async def test_delete_kitten(async_client: AsyncClient):
    breed_response = await async_client.post('/api/v1/breeds', json={'name': 'Maine Coon'})
    breed_id = breed_response.json()['id']

    data = {
        'name': 'Snow',
        'color': 'white',
        'age': 6,
        'description': 'sleepy',
        'breed_id': breed_id,
    }
    create_response = await async_client.post('/api/v1/kittens', json=data)
    kitten_id = create_response.json()['id']

    response = await async_client.delete(f'/api/v1/kittens/{kitten_id}')
    assert response.status_code == 200
    assert response.json()['message'] == 'Kitten deleted successfully'
