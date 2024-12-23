from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class BaseEntity:
    oid: str = field(
        default_factory=lambda: str(uuid4()),
        kw_only=True,
    )
