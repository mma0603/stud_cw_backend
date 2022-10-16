import enum


class OrderStatus(str, enum.Enum):  # noqa: WPS600

    processing = 'processing'
    transiting = 'transiting'
    delivered = 'delivered'
