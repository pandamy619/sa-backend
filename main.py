from fastapi import FastAPI

from routers import files


def main():
    """Makes the application running. Returns it to use during testing."""
    app = FastAPI()
    app.include_router(files.router)
    return app
