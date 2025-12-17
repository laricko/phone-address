from __future__ import annotations

import redis.asyncio as redis

from models import AddressPhone


class AddressPhoneRepository:
    def __init__(self, client: redis.Redis, *, prefix: str = "address"):
        self.client = client
        self.prefix = prefix

    def _build_key(self, phone_number: str) -> str:
        return f"{self.prefix}:{phone_number}"

    async def get_by_phone_number(self, phone_number: str) -> AddressPhone | None:
        key = self._build_key(phone_number)
        stored_address = await self.client.get(key)
        if stored_address is None:
            return None
        return AddressPhone(phone_number=phone_number, address=stored_address)

    async def create(self, address: AddressPhone) -> AddressPhone:
        key = self._build_key(address.phone_number)
        await self.client.set(key, address.address)
        return address

    async def update(self, address: AddressPhone) -> AddressPhone:
        key = self._build_key(address.phone_number)
        await self.client.set(key, address.address)
        return address

    async def delete(self, phone_number: str) -> None:
        key = self._build_key(phone_number)
        await self.client.delete(key)
