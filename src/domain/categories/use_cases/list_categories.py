
from attr import define

from src.domain.categories.dto.output import CategoryOutSchema
from src.domain.categories.interfaces import ICategoryRepo


@define
class ListCategories:
    category_repo: ICategoryRepo

    async def __call__(self) -> list[CategoryOutSchema]:
        categories = await self.category_repo.get_categories()
        return [CategoryOutSchema.from_entity(category) for category in categories]
