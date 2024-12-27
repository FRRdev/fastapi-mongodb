from collections.abc import Sequence
from typing import Protocol

from src.domain.categories.dto.filter import CategoryFilterSchema
from src.domain.categories.dto.input import CategoryInSchema
from src.domain.categories.entity import Category


class ICreateCategory(Protocol):
    async def __call__(self, schema: CategoryInSchema) -> Category: ...


class IListCategories(Protocol):
    async def __call__(
        self,
        params: CategoryFilterSchema,
    ) -> tuple[Sequence[Category], int]: ...


class ICategoryRepo(Protocol):
    async def get_categories(
        self,
        filters: CategoryFilterSchema,
    ) -> tuple[Sequence[Category], int]: ...

    async def add_category(self, category: Category) -> None: ...

    async def check_category_exists_by_name(self, name: str) -> bool: ...

    async def check_category_exists_by_oid(self, oid: str) -> bool: ...
