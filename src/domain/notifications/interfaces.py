from typing import Protocol


class IConsumeAndCreateNotification(Protocol):
    async def __call__(self) -> None: ...
