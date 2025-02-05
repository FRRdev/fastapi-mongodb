from dataclasses import dataclass

from src.utils.entity import BaseEntity


@dataclass
class User(BaseEntity):
    email: str
