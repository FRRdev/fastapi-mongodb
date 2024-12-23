from src.utils.exceptions.domain_exceptions import DomainException


class CategoryExistsException(DomainException):
    def __init__(self, name: str):
        self.message = f"Category with name '{name}' already exists"
        super().__init__(self.message)
