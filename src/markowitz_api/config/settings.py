import functools

import pydantic_settings


class ServiceSettings(pydantic_settings.BaseSettings):
    """Base settings for the service."""

    PROJECT_NAME: str = "Markowitz API"


@functools.lru_cache(maxsize=1)
def get_settings() -> ServiceSettings:
    """Get the service settings."""
    return ServiceSettings()
