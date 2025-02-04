from collections.abc import AsyncGenerator
from dataclasses import dataclass
from types import TracebackType
from typing import Self

import orjson
from aiokafka import AIOKafkaConsumer, AIOKafkaProducer


@dataclass
class KafkaMessageBroker:
    producer: AIOKafkaProducer
    consumer: AIOKafkaConsumer

    async def send_message(self, key: bytes, topic: str, value: bytes) -> None:
        await self.producer.send_and_wait(key=key, topic=topic, value=value)

    async def start_consuming(self, topic: str) -> AsyncGenerator[dict, None]:
        self.consumer.subscribe(topics=[topic])

        async for message in self.consumer:
            yield orjson.loads(message.value)

    async def stop_consuming(self) -> None:
        self.consumer.unsubscribe()

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None:
        await self.producer.stop()
        await self.consumer.stop()

    async def __aenter__(self) -> Self:
        await self.producer.start()
        await self.consumer.start()
        return self
