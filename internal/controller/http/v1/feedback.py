from typing import List
from uuid import UUID

from fastapi import APIRouter, Depends

from internal.dto.feedback import (
    FeedbackBody,
    FeedbackCreate,
    FeedbackRead,
)
from internal.dto.user.request import RequestUser
from internal.entity.feedback import Feedback
from internal.service.feedback import FeedbackService
from internal.usecase.utils import dependencies

router = APIRouter()


@router.post(
    path='',
    response_model=FeedbackRead,
)
async def create_feedback(
    dto: FeedbackBody,
    feedback_service: FeedbackService = Depends(),
    request_user: RequestUser = Depends(dependencies.get_request_user),
) -> Feedback:
    return await feedback_service.create(
        FeedbackCreate.from_body(request_user.id, dto),
    )


@router.get(
    path='/{product_id}',
    response_model=List[FeedbackRead],
)
async def read_feedbacks(
    product_id: UUID,
    feedback_service: FeedbackService = Depends(),
    _: RequestUser = Depends(dependencies.get_request_user),
) -> List[Feedback]:
    return await feedback_service.find(product_id)
