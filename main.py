from fastapi import FastAPI

from routers import files


def main() -> FastAPI:
    """Makes the application running. Returns it to use during testing."""
    app = FastAPI()
    app.include_router(files.router)
    return app
