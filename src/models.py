from pydantic import BaseModel, Field


class AddressPhone(BaseModel):
    phone_number: str = Field(..., description="Phone number used as the key")
    address: str = Field(
        ..., description="Full address associated with the phone number"
    )


class AddressUpdate(BaseModel):
    address: str = Field(..., description="New address for the phone number")
