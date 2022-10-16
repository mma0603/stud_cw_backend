import sqlalchemy as sa
from sqlalchemy.dialects import postgresql as psql

from internal.entity.base import Base
from internal.entity.mixin import TimestampMixin
from internal.entity.role import Role


class User(TimestampMixin, Base):

    username = sa.Column(sa.String(100), nullable=False)
    password = sa.Column(sa.String(64), nullable=False)
    email = sa.Column(sa.String(255), nullable=False)

    role = sa.Column(
        psql.ENUM(Role, name='role'), default=Role.user, nullable=False,
    )

    first_name = sa.Column(sa.String(100))
    last_name = sa.Column(sa.String(100))

    address = sa.Column(sa.Text)
