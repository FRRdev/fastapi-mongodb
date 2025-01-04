from collections.abc import Sequence
from dataclasses import dataclass

from src.domain.products.entity import Product
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.products.converters import (
    convert_product_document_to_entity,
    convert_product_entity_to_document,
    convert_sample_product_document_to_entity,
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

    async def check_products_exists_by_slug(self, slug: str) -> bool:
        return bool(
            await self._collection.find_one(
                filter={"slug": slug},
            ),
        )

    async def get_products_by_slug_regex(self, slug: str) -> Sequence[Product]:
        return [
            convert_sample_product_document_to_entity(product_document)
            async for product_document in self._collection.find(
                {"slug": {"$regex": slug}},
            )
        ]


