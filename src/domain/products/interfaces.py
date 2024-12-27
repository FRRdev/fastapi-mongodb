from collections.abc import Sequence
from typing import Protocol

from src.domain.categories.entity import Category
from src.domain.products.dto.input import ProductInSchema
from src.domain.products.entity import Product


class ICreateProduct(Protocol):
    async def __call__(self, schema: ProductInSchema) -> Product: ...


class IListProducts(Protocol):
    async def __call__(self) -> Sequence[Product]: ...


class IProductRepo(Protocol):
    async def get_products(self) -> Sequence[Category]: ...

    async def add_product(self, product: Product) -> None: ...

