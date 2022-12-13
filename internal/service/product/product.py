from typing import List
from uuid import UUID

from fastapi import Depends
from pytorm.repository import InjectRepository
from sqlalchemy.ext.asyncio import AsyncSession

from internal.dto.product import ProductCreate, ProductUpdate
from internal.entity.product import Product
from internal.usecase.utils import get_session


class ProductService(object):  # noqa: WPS214

    def __init__(
        self, session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session
        self.repository = InjectRepository(Product, session)

    async def find(self, **attrs) -> List[Product]:
        return await self.repository.find(**attrs)

    async def create(self, dto: ProductCreate) -> Product:
        product = self.repository.create(**dto.dict())
        product = await self.repository.save(product)
        return await self.repository.find_one(id=product.id)

    async def update(self, product_id: UUID, dto: ProductUpdate) -> Product:
        product = self.repository.create(id=product_id, **dto.dict())
        return await self.repository.save(product)
