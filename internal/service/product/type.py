from typing import List
from uuid import UUID

from fastapi import Depends
from pytorm.repository import InjectRepository
from sqlalchemy.ext.asyncio import AsyncSession

from internal.dto.product.type import (
    ProductTypeCreate,
    ProductTypeUpdate,
)
from internal.entity.product.type import ProductType
from internal.usecase.utils import get_session


class ProductTypeService(object):  # noqa: WPS214

    def __init__(
        self, session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session
        self.repository = InjectRepository(ProductType, session)

    async def find(self, **attrs) -> List[ProductType]:
        return await self.repository.find(**attrs)

    async def create(self, dto: ProductTypeCreate) -> ProductType:
        product_type = self.repository.create(**dto.dict())
        return await self.repository.save(product_type)

    async def update(
        self, product_type_id: UUID, dto: ProductTypeUpdate,
    ) -> ProductType:
        product_type = self.repository.create(id=product_type_id, **dto.dict())
        return await self.repository.save(product_type)
