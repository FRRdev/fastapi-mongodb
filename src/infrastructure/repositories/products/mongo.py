from dataclasses import dataclass

from src.domain.products.entity import Product
from src.infrastructure.repositories.base import BaseMongoDBRepository
from src.infrastructure.repositories.products.converters import (
    convert_product_entity_to_document,
)


@dataclass
class MongoDBProductsRepository(BaseMongoDBRepository):
    async def add_product(self, product: Product) -> None:
        await self._collection.insert_one(convert_product_entity_to_document(product))
