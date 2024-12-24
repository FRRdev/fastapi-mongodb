from attr import define

from src.domain.categories.dto.input import CategoryInSchema
from src.domain.categories.entity import Category
from src.domain.categories.exceptions import CategoryExistsException
from src.domain.categories.interfaces import ICategoryRepo


@define
class CreateCategory:
    category_repo: ICategoryRepo

    async def __call__(self, schema: CategoryInSchema) -> Category:
        if await self.category_repo.check_category_exists_by_name(schema.name):
            raise CategoryExistsException(schema.name)
        category = Category(name=schema.name, order=schema.order)
        await self.category_repo.add_category(category)
        return category
