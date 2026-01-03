Задание было выполнено в качестве тестового задания для одной компании.

# Phone Address Service

Небольшой сервис на FastAPI для хранения связок "телефон — адрес" в Redis.

## Запуск

### Docker Compose
1. Соберите и запустите сервис и Redis:
```bash
docker compose up --build
```
2. API будет доступно по адресу `http://localhost:8000`.


## Эндпоинты
- `GET /addresses/{phone}` — получить адрес по номеру телефона.
- `POST /addresses/` — создать связку (поля `phone_number`, `address`).
- `PUT /addresses/{phone}` — обновить адрес (тело: `address`).
- `DELETE /addresses/{phone}` — удалить запись.`


## Тестирование и линтинг

- uv run mypy src
- uv run black src
- uv run isort src
