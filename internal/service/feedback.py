from typing import List
from uuid import UUID

from fastapi import Depends
from pytorm.repository import InjectRepository
from sqlalchemy.ext.asyncio import AsyncSession

from internal.dto.feedback import FeedbackCreate
from internal.entity.feedback import Feedback
from internal.usecase.utils import get_session


class FeedbackService(object):  # noqa: WPS214

    def __init__(
        self, session: AsyncSession = Depends(get_session),
    ) -> None:
        self.session = session
        self.repository = InjectRepository(Feedback, session)

    async def create(self, dto: FeedbackCreate) -> Feedback:
        feedback = self.repository.create(**dto.dict())
        await self.repository.save(feedback)
        return await self.repository.find_one(id=feedback.id)

    async def find(self, product_id: UUID) -> List[Feedback]:
        return await self.repository.find(product_id=product_id)
