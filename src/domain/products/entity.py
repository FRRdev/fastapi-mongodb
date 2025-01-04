from dataclasses import dataclass
from decimal import Decimal

from src.domain.categories.entity import Category
from src.utils.entity import BaseEntity


@dataclass
class Product(BaseEntity):
    name: str
    price: Decimal
    slug: str | None = None
    category_id: str | None = None
    category: Category | None = None
