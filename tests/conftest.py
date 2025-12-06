from unittest.mock import AsyncMock

import pytest

from protocols import AddressPhoneRepositoryProtocol
from services import AddressPhoneService


@pytest.fixture
def address_phone_repository_mock():
    repo = AsyncMock(spec=AddressPhoneRepositoryProtocol)
    return repo


@pytest.fixture
def address_phone_service(address_phone_repository_mock):
    return AddressPhoneService(address_phone_repository=address_phone_repository_mock)
