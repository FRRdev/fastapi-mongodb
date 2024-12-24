from collections.abc import Sequence

from attr import define

from src.domain.categories.dto.filter import CategoryFilterSchema
from src.domain.categories.entity import Category
from src.domain.categories.interfaces import ICategoryRepo


@define
class ListCategories:
    category_repo: ICategoryRepo

    async def __call__(
        self,
        params: CategoryFilterSchema,
    ) -> tuple[Sequence[Category], int]:
        return await self.category_repo.get_categories(params)
