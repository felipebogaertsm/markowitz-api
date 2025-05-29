import fastapi

from markowitz_api.config import settings


def create_app() -> fastapi.FastAPI:
    """
    Creates the main FastAPI application instance.

    Returns:
        FastAPI: The FastAPI application instance.
    """
    cfg = settings.get_settings()
    return fastapi.FastAPI(title=cfg.PROJECT_NAME)


app = create_app()
