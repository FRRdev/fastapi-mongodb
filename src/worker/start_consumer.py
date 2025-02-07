import asyncio

from dependency_injector.wiring import Provide, inject

from src.containers import container
from src.domain.notifications.interfaces import IConsumeAndCreateNotification


@inject
async def run(
    use_case: IConsumeAndCreateNotification = Provide[
        "use_cases.consume_and_create_notifications",
    ],
) -> None:
    await use_case()


if __name__ == "__main__":
    container.gateways.logging_setup.init()  # type: ignore[attr-defined]

    container.wire(modules=[__name__])
    asyncio.run(run())
