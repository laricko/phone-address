import pytest
from pydantic import ValidationError

from exceptions import AddressNotFound
from models import AddressPhone


@pytest.mark.asyncio
async def test_update_success(address_phone_service, address_phone_repository_mock):
    stored = AddressPhone(phone_number="+1234567890", address="Old Address")
    updated = AddressPhone(phone_number=stored.phone_number, address="New Address")
    address_phone_repository_mock.get_by_phone_number.return_value = stored
    address_phone_repository_mock.update.return_value = updated

    result = await address_phone_service.update_address(stored.phone_number, "New Address")

    assert result == updated
    address_phone_repository_mock.update.assert_awaited_once_with(updated)


@pytest.mark.asyncio
async def test_update_not_found(address_phone_service, address_phone_repository_mock):
    address_phone_repository_mock.get_by_phone_number.return_value = None

    with pytest.raises(AddressNotFound):
        await address_phone_service.update_address("+22222222222", "New Address")

    address_phone_repository_mock.update.assert_not_awaited()


@pytest.mark.asyncio
async def test_update_invalid_phone(address_phone_service, address_phone_repository_mock):
    address_phone_repository_mock.get_by_phone_number.return_value = AddressPhone(
        phone_number="+33333333333", address="Existing"
    )

    with pytest.raises(ValidationError):
        await address_phone_service.update_address("invalid", "New Address")

    address_phone_repository_mock.update.assert_not_awaited()
