import enum


class Role(str, enum.Enum):  # noqa: WPS600

    user = 'user'
    manager = 'manager'
