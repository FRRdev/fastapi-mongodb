from src.utils.exceptions.domain_exceptions import DomainException
from src.utils.exceptions.repository_exceptions import ObjectExistsException


class UserExistsException(DomainException):
    def __init__(self, name: str):
        self.message = f"User with email '{name}' already exists"
        super().__init__(self.message)


class UserExistsRepositoryException(ObjectExistsException): ...
