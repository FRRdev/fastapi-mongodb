class BaseHTTPException(Exception):  # noqa: N818
    status: int
    message: str
