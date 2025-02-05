from pydantic import BaseModel

from src.domain.users.entity import User


class UserOutSchema(BaseModel):
    oid: str
    email: str

    @classmethod
    def from_entity(cls, user: User) -> "UserOutSchema":
        return UserOutSchema(
            oid=user.oid,
            email=user.email,
        )
