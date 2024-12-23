from collections.abc import Sequence
from dataclasses import dataclass

from src.domain.categories.entity import Category
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.categories.converters import (
    convert_category_entity_to_document,
)


@dataclass
class MongoDBCategoriesRepository(BaseMongoDBRepository):
    async def get_categories(self) -> Sequence[Category]:
        return self._collection.find()

    async def add_category(self, category: Category) -> None:
        await self._collection.insert_one(convert_category_entity_to_document(category))

    async def check_category_exists_by_name(self, name: str) -> bool:
        return bool(
            await self._collection.find_one(
                filter={"name": name},
            ),
        )
