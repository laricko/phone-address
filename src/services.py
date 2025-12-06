from protocols import AddressPhoneRepositoryProtocol


class AddressPhoneService:
    def __init__(self, address_phone_repository: AddressPhoneRepositoryProtocol):
        self.address_phone_repository = address_phone_repository

    