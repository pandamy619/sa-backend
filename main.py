from fastapi import FastAPI

from routers import files
import file_related.functions as file_functions


def main() -> FastAPI:
    """Makes the application running. Returns it to use during testing."""
    file_functions.create_dir_for_uploads()
    app = FastAPI()
    app.include_router(files.router)
    return app
