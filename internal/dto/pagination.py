from pydantic import BaseModel
from fastapi_pagination import Params


class Pagination(BaseModel):

    limit: int
    offset: int

    @classmethod
    def from_params(cls, params: Params) -> 'Pagination':
        return cls(
            limit=params.size,
            offset=(params.page - 1) * params.size,
        )
