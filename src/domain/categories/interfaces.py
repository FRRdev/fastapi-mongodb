from collections.abc import Sequence
from typing import Protocol

from src.domain.categories.dto.input import CategoryInSchema
from src.domain.categories.dto.output import CategoryOutSchema
from src.domain.categories.entity import Category


class ICreateCategory(Protocol):
    async def __call__(self, schema: CategoryInSchema) -> Category:
        ...



class IListCategories(Protocol):
    async def __call__(self) -> list[CategoryOutSchema]:
        ...


class ICategoryRepo(Protocol):
    async def get_categories(self) -> Sequence[Category]: ...

    async def add_category(self, category: Category) -> None: ...

    async def check_category_exists_by_name(self, name: str) -> bool:
        ...
