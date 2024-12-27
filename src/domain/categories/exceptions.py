from src.utils.exceptions.domain_exceptions import DomainException


class CategoryExistsException(DomainException):
    def __init__(self, name: str):
        self.message = f"Category with name '{name}' already exists"
        super().__init__(self.message)


class CategoryDoesNotExistsException(DomainException):
    def __init__(self, oid: str):
        self.message = f"Category with id '{oid}' does not exist"
        super().__init__(self.message)
