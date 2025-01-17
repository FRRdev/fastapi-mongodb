from decimal import Decimal

from pydantic import BaseModel, Field, RootModel

from src.domain.categories.dto.output import CategorySampleOutSchema
from src.domain.products.entity import Product


class BaseProductOutSchema(BaseModel):
    oid: str
    name: str
    price: Decimal = Field(max_digits=5, decimal_places=2)
    slug: str | None = None


class ProductOutSchema(BaseProductOutSchema):
    category_id: str

    @classmethod
    def from_entity(cls, product: Product) -> "ProductOutSchema":
        return ProductOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            category_id=product.category_id,  # type: ignore[arg-type]
        )


class ProductFullOutSchema(BaseProductOutSchema):
    category: CategorySampleOutSchema
    discount_price: Decimal | None = Field(max_digits=5, decimal_places=2)

    @classmethod
    def from_entity(cls, product: Product) -> "ProductFullOutSchema":
        return ProductFullOutSchema(
            oid=product.oid,
            name=product.name,
            price=product.price,
            discount_price=product.discount_price,
            slug=product.slug,
            category=CategorySampleOutSchema.from_entity(product.category),  # type: ignore[arg-type]
        )


class ProductListOutSchema(RootModel):
    root: list[ProductFullOutSchema]
