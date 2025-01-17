from dataclasses import dataclass

from src.utils.entity import BaseEntity


@dataclass
class Discount(BaseEntity):
    percent: int
