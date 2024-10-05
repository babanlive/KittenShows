# kitten shows

## Описание проекта

Проект представляет из себя веб-приложение, которое предоставляет REST API для администратора онлайн выставки котят. С помощью данного приложения можно управлять информацией о породах и котятах.

## Функциональность:

- Получение списка пород.
- Получение списка всех котят.
- Получение списка котят определенной породы по фильтру.
- Получение подробной информации о котенке.
- Добавление информации о котенке.
- Изменение информации о котенке.
- Удаление информации о котенке.

## Технологии и инструменты

- Python 3.12
- FastAPI
- Pre-commit
- Ruff
- Postgres
- Docker

## Установка и запуск проекта

1. Клонируйте репозиторий и перейдите в папку проекта:

    ```shell
    git clone git@github.com:babanlive/KittenShows.git && cd KittenShows
    ```

2. Создание файла .env
   - Создайте в папке приложения файл `.env` согласно образцу [.env_example](.env.example).

3. Запуск проекта через Docker
   - Для запуска в режиме разработки выполните команду:

    ```shell
    docker-compose -f docker-compose.dev.yaml up --build
    ```

   - Для запуска в режиме производства выполните команду:

    ```shell
    docker-compose -f docker-compose.prod.yaml up --build
    ```

4. Выполните миграции:

    ```shell
    docker exec -it app_fastapi poetry run alembic upgrade head
    ```

## Работа с API:

### Базовый URL

API доступно по адресу:

```shell
http://127.0.0.1:8000/api/v1/
```

### Документация API доступна в формате Swagger по следующему адресу:

```shell
http://127.0.0.1:8000/docs
```
### Запросы к API:

- GET /breeds — Получение списка всех пород котят.
- GET /kittens — Получение списка всех котят.
- GET /kittens/{kitten_id} — Получение подробной информации о котенке.
- POST /kittens — Добавление нового котенка.
- PUT /kittens/{kitten_id} — Обновление информации о котенке.
- DELETE /kittens/{kitten_id} — Удаление котенка.


### Примеры запросов
1. Получение списка пород котят

```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/api/v1/breeds' \
  -H 'accept: application/json'
  ```

2. Добавление породы котят
```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/api/v1/breeds' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "maine coon"
}'
 ```

3. Добавление нового котенка

```shell
curl -X 'POST' \
  'http://127.0.0.1:8000/api/api/v1/kittens' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Pushok",
  "color": "grey",
  "age": 5,
  "description": "",
  "breed_id": 1
}'
 ```

 4. Получение информации о котенке с фильтрацией по минимальному возрасту

```shell
curl -X 'GET' \
  'http://127.0.0.1:8000/api/api/v1/kittens?min_age=2' \
  -H 'accept: application/json'
 ```
 
  5. Обновление информации о котенке

```shell
curl -X 'PUT' \
  'http://127.0.0.1:8000/api/api/v1/kittens/1' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "name": "Snegok",
    "age": 4,
    "color": "white",
    "breed_id": 1
}'
 ```
 
6. Удаление котенка

```shell
curl -X 'DELETE' \
  'http://127.0.0.1:8000/api/api/v1/kittens/1' \
  -H 'accept: application/json'
 ```

