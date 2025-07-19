"""
Application configuration using Pydantic Settings.
"""

from typing import List

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings."""

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )

    PROJECT_NAME: str = "FastAPI Template"
    API_V1_STR: str = "/api/v1"

    # CORS settings - simplified for now
    BACKEND_CORS_ORIGINS: List[str] = [
        "http://localhost:3000",  # React default
        "http://localhost:8080",  # Vue default
        "http://localhost:4200",  # Angular default
    ]

    # Environment
    ENVIRONMENT: str = "development"
    DEBUG: bool = True


# Create settings instance
settings = Settings()
