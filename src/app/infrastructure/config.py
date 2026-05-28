from dature import load, EnvFileSource, F
from dature.fields.secret_str import SecretStr
from dataclasses import dataclass
from pathlib import Path

_ENV_CONFIG = Path(__file__).parents[3] / ".env"

@dataclass
class TelegramConfig:
    bot_token: SecretStr

@dataclass
class Config:
    telegram: TelegramConfig

def load_config():
    telegram = load(
        EnvFileSource(file=_ENV_CONFIG, 
                      field_mapping={
                          F[TelegramConfig].bot_token: "BOT_TOKEN"
                      }), 
        schema=TelegramConfig
    )
    return Config(telegram=telegram)

config = load_config()