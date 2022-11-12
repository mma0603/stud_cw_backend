from typing import Any, Dict
from uuid import UUID

from pydantic import BaseModel, EmailStr, constr, validator

from internal.entity.role import Role
from internal.usecase.utils import hashing


class BaseUser(BaseModel):

    username: constr(max_length=50)
    email: constr(max_length=100)

    role: Role

    first_name: constr(max_length=50)
    last_name: constr(max_length=50)

    address: constr(max_length=255)


class UserRead(BaseUser):

    id: UUID

    class Config(object):
        orm_mode = True


class UserAuth(BaseModel):

    username: constr(strip_whitespace=True, max_length=50)
    password: str

    @validator('password')
    def hashing_password(cls, v: str) -> str:  # noqa: N805
        return hashing.pbkdf2_hmac(v)


class UserCreate(BaseModel):

    username: constr(strip_whitespace=True, max_length=50)
    password: str
    email: EmailStr

    @validator('password')
    def hashing_password(cls, v: str) -> str:  # noqa: N805
        return hashing.pbkdf2_hmac(v)


class UserUpdate(BaseModel):

    username: constr(strip_whitespace=True, max_length=50) | None
    password: str | None
    email: EmailStr | None

    first_name: constr(max_length=50) | None
    last_name: constr(max_length=50) | None

    address: constr(max_length=255) | None

    def dict(self, **kwargs) -> Dict[str, Any]:
        return super().dict(exclude_unset=True, **kwargs)

    @validator('password')
    def hashing_password(cls, v: str | None) -> str | None:  # noqa: N805
        if v is not None:
            return hashing.pbkdf2_hmac(v)
