from attr import define

from src.domain.products.interfaces import IMessageBroker


@define
class ConsumeAndCreateNotifications:
    message_broker: IMessageBroker

    async def __call__(self):
        async for _msg in self.message_broker.start_consuming("products"):  # type: ignore[attr-defined]
            pass
