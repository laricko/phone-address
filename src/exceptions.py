class AddressPhoneError(Exception):
    """Base class for phone-address domain errors."""


class AddressNotFound(AddressPhoneError):
    def __init__(self, phone_number: str, message: str = "Phone number not found"):
        self.phone_number = phone_number
        super().__init__(message)


class AddressAlreadyExists(AddressPhoneError):
    def __init__(self, phone_number: str, message: str = "Phone number already exists"):
        self.phone_number = phone_number
        super().__init__(message)
