# Phone Address Service

Небольшой сервис на FastAPI для хранения связок "телефон — адрес" в Redis.

## Запуск

### Docker Compose
1. Соберите и запустите сервис и Redis:
   ```bash
docker compose up --build
   ```
2. API будет доступно по адресу `http://localhost:8000`.

### Локально
1. Установите зависимости:
   ```bash
pip install .
   ```
2. Запустите приложение:
   ```bash
REDIS_URL=redis://localhost:6379/0 uvicorn src.api:app --reload
   ```

## Эндпоинты
- `GET /addresses/{phone}` — получить адрес по номеру телефона.
- `POST /addresses/` — создать связку (поля `phone_number`, `address`).
- `PUT /addresses/{phone}` — обновить адрес (тело: `address`).
- `DELETE /addresses/{phone}` — удалить запись.
