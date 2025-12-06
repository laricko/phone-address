import pytest

from exceptions import AddressNotFound
from models import AddressPhone


@pytest.mark.asyncio
async def test_delete_success(address_phone_service, address_phone_repository_mock):
    stored = AddressPhone(phone_number="+1234567890", address="123 Main St")
    address_phone_repository_mock.get_by_phone_number.return_value = stored

    await address_phone_service.delete_address(stored.phone_number)

    address_phone_repository_mock.delete.assert_awaited_once_with(stored.phone_number)


@pytest.mark.asyncio
async def test_delete_not_found(address_phone_service, address_phone_repository_mock):
    address_phone_repository_mock.get_by_phone_number.return_value = None

    with pytest.raises(AddressNotFound):
        await address_phone_service.delete_address("+99999999999")

    address_phone_repository_mock.delete.assert_not_awaited()
