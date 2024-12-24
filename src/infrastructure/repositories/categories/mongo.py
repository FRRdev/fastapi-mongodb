from collections.abc import Sequence
from dataclasses import dataclass

from src.domain.categories.dto.filter import CategoryFilterSchema
from src.domain.categories.entity import Category
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.categories.converters import (
    convert_category_document_to_entity,
    convert_category_entity_to_document,
)


@dataclass
class MongoDBCategoriesRepository(BaseMongoDBRepository):
    async def get_categories(
        self,
        filters: CategoryFilterSchema,
    ) -> tuple[Sequence[Category], int]:
        pipeline = [
            {
                "$lookup": {
                    "from": "product",
                    "localField": "_id",
                    "foreignField": "category",
                    "as": "products",
                },
            },
            {
                "$addFields": {
                    "product_count": {"$size": "$products"},
                },
            },
            {"$project": {"products": 0}},
            {"$sort": {"order": 1}},
            {"$skip": filters.offset},
            {"$limit": filters.limit},
        ]
        count = await self._collection.count_documents({})
        categories = [
            convert_category_document_to_entity(category_document)
            async for category_document in self._collection.aggregate(pipeline)
        ]
        return categories, count

    async def add_category(self, category: Category) -> None:
        await self._collection.insert_one(convert_category_entity_to_document(category))

    async def check_category_exists_by_name(self, name: str) -> bool:
        return bool(
            await self._collection.find_one(
                filter={"name": name},
            ),
        )
