from fastapi import Depends, FastAPI

from models import AddressPhone
from services import AddressService

app = FastAPI()

address_repository = ...


@app.post("/addresses/")
async def create_address(data: AddressPhone):
    return await ...
