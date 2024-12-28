from pydantic import BaseModel

from src.domain.categories.entity import Category


class BaseCategoryOutSchema(BaseModel):
    oid: str
    name: str
    order: int


class CategorySampleOutSchema(BaseCategoryOutSchema):
    @classmethod
    def from_entity(cls, category: Category) -> "CategorySampleOutSchema":
        return CategorySampleOutSchema(
            oid=category.oid,
            name=category.name,
            order=category.order,
        )


class CategoryOutSchema(BaseCategoryOutSchema):
    product_count: int | None = None

    @classmethod
    def from_entity(cls, category: Category) -> "CategoryOutSchema":
        return CategoryOutSchema(
            oid=category.oid,
            name=category.name,
            order=category.order,
            product_count=category.product_count,
        )


class CategoryListOutSchema(BaseModel):
    count: int
    next_page: bool
    items: list[CategoryOutSchema]
