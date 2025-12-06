import pytest
from pydantic import ValidationError

from models import AddressPhone


def test_phone_number_validation():
    with pytest.raises(ValidationError):
        AddressPhone(phone_number="not-a-phone", address="Somewhere")


def test_phone_number_accepts_e164_pattern():
    model = AddressPhone(phone_number="+12345678901", address="Valid")

    assert model.phone_number == "+12345678901"
    assert model.address == "Valid"
