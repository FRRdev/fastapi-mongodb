from src.utils.exceptions.base_exceptions import BaseException


class ObjectExistsException(BaseException):
    pass


class NoFieldException(BaseException):
    def __init__(self, field: str):
        self.field = field


class NotFoundException(BaseException):
    pass
