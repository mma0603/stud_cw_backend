from uuid import UUID

from pydantic import BaseModel, conint

from internal.dto.user import UserRead


class BaseFeedback(BaseModel):

    text: str | None
    mark: conint(ge=1, le=5)

    user: UserRead


class FeedbackRead(BaseFeedback):

    id: UUID

    class Config(object):
        orm_mode = True


class FeedbackBody(BaseModel):

    text: str | None
    mark: conint(ge=1, le=5)

    product_id: UUID


class FeedbackCreate(FeedbackBody):

    user_id: UUID

    @classmethod
    def from_body(cls, user_id: UUID, dto: FeedbackBody) -> 'FeedbackCreate':
        return cls(user_id=user_id, **dto.dict())
