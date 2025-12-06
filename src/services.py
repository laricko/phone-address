from exceptions import AddressAlreadyExists, AddressNotFound
from models import AddressPhone
from protocols import AddressPhoneRepositoryProtocol


class AddressPhoneService:
    def __init__(self, address_phone_repository: AddressPhoneRepositoryProtocol):
        self.address_phone_repository = address_phone_repository

    async def get_address(self, phone_number: str) -> AddressPhone:
        stored = await self.address_phone_repository.get_by_phone_number(phone_number)
        if stored is None:
            raise AddressNotFound(phone_number)
        return stored

    async def create_address(self, address: AddressPhone) -> AddressPhone:
        stored = await self.address_phone_repository.get_by_phone_number(
            address.phone_number
        )
        if stored:
            raise AddressAlreadyExists(address.phone_number)
        return await self.address_phone_repository.create(address)

    async def update_address(self, phone_number: str, address: str) -> AddressPhone:
        stored = await self.address_phone_repository.get_by_phone_number(phone_number)
        if stored is None:
            raise AddressNotFound(phone_number)
        updated = AddressPhone(phone_number=phone_number, address=address)
        return await self.address_phone_repository.update(updated)

    async def delete_address(self, phone_number: str) -> None:
        stored = await self.address_phone_repository.get_by_phone_number(phone_number)
        if stored is None:
            raise AddressNotFound(phone_number)
        await self.address_phone_repository.delete(phone_number)
