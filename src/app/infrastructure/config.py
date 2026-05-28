from dature import load, EnvFileSource, F, Toml10Source
from dature.fields.secret_str import SecretStr
from dataclasses import dataclass
from pathlib import Path
from sqlalchemy import URL

_ENV_CONFIG = Path(__file__).parents[3] / ".env"
_TOML_CONFIG = Path(__file__).parents[3] / "config.toml"

@dataclass
class TelegramConfig:
    bot_token: SecretStr

@dataclass
class DatabaseConfig:
    name: str
    username: str
    host: str
    port: int
    password: SecretStr

    @property
    def get_url(self) -> URL:
        return URL.create(
            drivername="postgresql+asyncpg",
            username=self.username,
            password=self.password.get_secret_value(),
            host=self.host,
            port=self.port,
            database=self.name,
        )

@dataclass
class Config:
    telegram: TelegramConfig
    database: DatabaseConfig

def load_config():
    telegram = load(
        EnvFileSource(
            file=_ENV_CONFIG, 
            field_mapping={
            F[TelegramConfig].bot_token: "BOT_TOKEN"
            }
        ), 
        schema=TelegramConfig
    )
    database = load(
        EnvFileSource(
            file=_ENV_CONFIG, 
            field_mapping={
            F[DatabaseConfig].password: "DB_PASSWORD"
            }
        ), 
        Toml10Source(file=_TOML_CONFIG, prefix="database"), 
        schema=DatabaseConfig
    )
    return Config(telegram=telegram, database=database)

config = load_config()