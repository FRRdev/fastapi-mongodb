from collections.abc import AsyncGenerator

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer

from src.infrastructure.message_brokers.kafka import KafkaMessageBroker


async def init_kafka_message_broker(
    kafka_producer: AIOKafkaProducer,
    kafka_consumer: AIOKafkaConsumer,
) -> AsyncGenerator[KafkaMessageBroker, None]:
    async with KafkaMessageBroker(
        producer=kafka_producer,
        consumer=kafka_consumer,
    ) as message_broker:
        yield message_broker
