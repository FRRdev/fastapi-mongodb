from collections.abc import Sequence
from typing import Protocol

from src.domain.products.dto.input import ProductInSchema
from src.domain.products.entity import Product


class ICreateProduct(Protocol):
    async def __call__(self, schema: ProductInSchema) -> Product: ...


class IListProducts(Protocol):
    async def __call__(self) -> Sequence[Product]: ...


class IProductRepo(Protocol):
    async def get_products(self) -> Sequence[Product]: ...

    async def add_product(self, product: Product) -> None: ...

    async def get_products_by_slug_regex(self, slug: str) -> Sequence[Product]: ...

    async def check_products_exists_by_slug(self, slug: str) -> bool: ...


class ISlugifier(Protocol):
    async def generate_slug(self, source: str) -> str: ...
