from uuid import UUID

from pydantic import BaseModel

from internal.dto.session import Session
from internal.entity.role import Role


class RequestUser(BaseModel):

    id: UUID
    role: Role
    session: Session

    @property
    def is_manager(self) -> bool:
        return self.role == Role.manager
