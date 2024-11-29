from collections.abc import Sequence
from pathlib import Path

from pydantic import HttpUrl, SecretStr, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).parent.parent.parent


class CryptConfig(BaseSettings):
    schemes: list[str] = ["bcrypt"]

    model_config = SettingsConfigDict(env_prefix="crypt_")


class SecurityConfig(BaseSettings):
    secret_key: SecretStr = SecretStr("secret")
    access_token_expires: int = 60 * 24 * 30
    algorithm: str = "HS256"

    model_config = SettingsConfigDict(env_prefix="security_")


class AppSettings(BaseSettings):
    name: str = "Catalog"
    root_path: str = ""
    debug: bool = False
    cors_origins: Sequence[str] | str = "*"

    model_config = SettingsConfigDict(env_prefix="app_")


class SentryConfig(BaseSettings):
    dsn: HttpUrl | None = None
    env: str | None = None

    model_config = SettingsConfigDict(env_prefix="sentry_")


class LoggingSettings(BaseSettings):
    serializer: bool = False
    level: str = "INFO"

    model_config = SettingsConfigDict(env_prefix="logging_")


class RabbitMQConfig(BaseSettings):
    user: str = "guest"
    password: str = "guest"
    host: str = "rabbitmq-catalog"
    port: str = "5672"
    default_exchange_name: str = "my_exchange"
    default_queue_name: str = "email_update"
    url: str | None = None

    class Config:
        env_prefix = "rabbitmq_"

    @field_validator("url")
    def assemble_url(cls, v, values):  # noqa: N805
        data = values.data
        return v or f"amqp://{data['user']}:{data['password']}@{data['host']}:{data['port']}"


class MongoDBConfig(BaseSettings):
    mongodb_connection_uri: str | None = None
    mongodb_admin_username: str | None = None
    mongodb_admin_password: str | None = None
    mongodb_product_database: str = "product"
    mongodb_product_collection: str = "product"
    mongodb_category_collection: str = "category"

    class Config:
        env_prefix = "mongodb_"
        env_file = ".env"


class Settings(BaseSettings):
    app: AppSettings = AppSettings()
    base_dir: Path = BASE_DIR
    sentry: SentryConfig = SentryConfig()
    crypt: CryptConfig = CryptConfig()
    security: SecurityConfig = SecurityConfig()
    logger: LoggingSettings = LoggingSettings()
    rabbitmq: RabbitMQConfig = RabbitMQConfig()
    mongodb: MongoDBConfig = MongoDBConfig()
