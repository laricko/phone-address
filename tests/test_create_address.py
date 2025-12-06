import pytest

from exceptions import AddressAlreadyExists
from models import AddressPhone


@pytest.mark.asyncio
async def test_create_success(address_phone_service, address_phone_repository_mock):
    address = AddressPhone(phone_number="+1234567890", address="123 Main St")
    address_phone_repository_mock.get_by_phone_number.return_value = None
    address_phone_repository_mock.create.return_value = address

    result = await address_phone_service.create_address(address)

    assert result == address
    address_phone_repository_mock.get_by_phone_number.assert_awaited_once_with(
        address.phone_number
    )
    address_phone_repository_mock.create.assert_awaited_once_with(address)


@pytest.mark.asyncio
async def test_create_duplicate(address_phone_service, address_phone_repository_mock):
    address = AddressPhone(phone_number="+19876543210", address="456 Oak St")
    address_phone_repository_mock.get_by_phone_number.return_value = address

    with pytest.raises(AddressAlreadyExists):
        await address_phone_service.create_address(address)

    address_phone_repository_mock.create.assert_not_awaited()
