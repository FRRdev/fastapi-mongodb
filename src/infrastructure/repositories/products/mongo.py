from collections.abc import Sequence
from dataclasses import dataclass

from src.domain.products.entity import Product
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.products.converters import (
    convert_product_document_to_entity,
    convert_product_entity_to_document,
)


@dataclass
class MongoDBProductsRepository(BaseMongoDBRepository):
    async def add_product(self, product: Product) -> None:
        await self._collection.insert_one(convert_product_entity_to_document(product))

    async def get_products(self) -> Sequence[Product]:
        pipeline = [
            {
                "$lookup": {
                    "from": "category",
                    "localField": "category_id",
                    "foreignField": "oid",
                    "as": "category",
                },
            },
            {"$unwind": "$category"},
        ]
        return [
            convert_product_document_to_entity(product_document)
            async for product_document in self._collection.aggregate(pipeline)
        ]
