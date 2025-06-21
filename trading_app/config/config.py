"""Configuration handling using Pydantic BaseSettings."""
from pydantic import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables or .env file."""

    alpaca_key: str
    alpaca_secret: str
    alpaca_endpoint: str = "https://paper-api.alpaca.markets"

    class Config:
        env_file = ".env"
        env_prefix = "TRADING_APP_"


settings = Settings()
