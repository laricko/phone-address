from pydantic import BaseModel


class AddressPhone(BaseModel):
    full_address: str
    phone_number: str
