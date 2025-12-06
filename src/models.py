from pydantic import BaseModel, Field


PHONE_NUMBER_PATTERN = r"^\+?[1-9]\d{6,14}$"


class AddressPhone(BaseModel):
    phone_number: str = Field(
        ...,
        pattern=PHONE_NUMBER_PATTERN,
        description="Phone number used as the key",
    )
    address: str = Field(
        ..., description="Full address associated with the phone number"
    )


class AddressUpdate(BaseModel):
    address: str = Field(..., description="New address for the phone number")
