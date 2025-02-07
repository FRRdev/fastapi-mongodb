from collections.abc import AsyncGenerator
from typing import Protocol

from src.domain.users.dto.input import UserInSchema
from src.domain.users.entity import User


class ICreateUser(Protocol):
    async def __call__(self, schema: UserInSchema) -> User: ...


class IUserRepo(Protocol):
    async def add_user(self, user: User) -> None: ...

    async def create_unique_email_constraint(self) -> None: ...

    async def get_user_ids(self) -> AsyncGenerator[str, None]: ...
