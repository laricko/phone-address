import os
from typing import AsyncGenerator

import redis.asyncio as redis
from fastapi import Depends, FastAPI, Request
from fastapi.responses import JSONResponse

from exceptions import AddressAlreadyExists, AddressNotFound
from models import AddressPhone, AddressUpdate
from repositories import AddressPhoneRepository
from services import AddressPhoneService

app = FastAPI()


async def get_redis_client() -> AsyncGenerator[redis.Redis]:
    redis_url = os.getenv("REDIS_URL", "redis://localhost:6379/0")
    client = redis.from_url(redis_url, decode_responses=True)
    try:
        yield client
    finally:
        await client.aclose()


def get_address_repository(
    client: redis.Redis = Depends(get_redis_client),
) -> AddressPhoneRepository:
    return AddressPhoneRepository(client)


def get_address_service(
    repository: AddressPhoneRepository = Depends(get_address_repository),
) -> AddressPhoneService:
    return AddressPhoneService(repository)


@app.exception_handler(AddressNotFound)
async def handle_not_found(
    request: Request, exc: AddressNotFound
) -> JSONResponse:
    return JSONResponse(status_code=404, content={"detail": str(exc)})


@app.exception_handler(AddressAlreadyExists)
async def handle_conflict(
    request: Request, exc: AddressAlreadyExists
) -> JSONResponse:
    return JSONResponse(status_code=409, content={"detail": str(exc)})


@app.get("/addresses/{phone_number}", response_model=AddressPhone)
async def retrieve_address(
    phone_number: str,
    service: AddressPhoneService = Depends(get_address_service),
):
    return await service.get_address(phone_number)


@app.post("/addresses/", response_model=AddressPhone, status_code=201)
async def create_address(
    data: AddressPhone,
    service: AddressPhoneService = Depends(get_address_service),
):
    return await service.create_address(data)


@app.put("/addresses/{phone_number}", response_model=AddressPhone)
async def update_address(
    phone_number: str,
    data: AddressUpdate,
    service: AddressPhoneService = Depends(get_address_service),
):
    return await service.update_address(phone_number, data.address)


@app.delete("/addresses/{phone_number}", status_code=204)
async def delete_address(
    phone_number: str,
    service: AddressPhoneService = Depends(get_address_service),
):
    await service.delete_address(phone_number)
    return None
