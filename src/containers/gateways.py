from uuid import uuid4

from aiokafka import AIOKafkaConsumer, AIOKafkaProducer
from dependency_injector import containers, providers
from motor.motor_asyncio import AsyncIOMotorClient

from src.infrastructure.message_brokers.factories import init_kafka_message_broker
from src.infrastructure.message_brokers.kafka import KafkaMessageBroker
from src.utils.logging import setup_logging
from src.utils.uvloop import activate_uvloop


class Gateways(containers.DeclarativeContainer):
    config = providers.Configuration()
    uvloop = providers.Resource(activate_uvloop)
    logging_setup = providers.Resource(setup_logging, config=config.logger)

    mongodb_client: providers.Provider[AsyncIOMotorClient] = providers.Singleton(
        AsyncIOMotorClient,
        config.mongodb.mongodb_connection_uri,
        serverSelectionTimeoutMS=3000,
    )

    kafka_producer: providers.Provider[AIOKafkaProducer] = providers.Singleton(
        AIOKafkaProducer,
        bootstrap_servers=config.kafka.kafka_url,
    )
    kafka_consumer: providers.Provider[AIOKafkaConsumer] = providers.Singleton(
        AIOKafkaConsumer,
        bootstrap_servers=config.kafka.kafka_url,
        group_id=f"chats-{uuid4()}",
        metadata_max_age_ms=30000,
    )
    message_broker: providers.Provider[KafkaMessageBroker] = providers.Resource(
        init_kafka_message_broker,
        kafka_producer=kafka_producer,
        kafka_consumer=kafka_consumer,
    )
