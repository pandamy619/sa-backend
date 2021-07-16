import os

from fastapi import File, UploadFile, status, HTTPException, APIRouter

import routers.file_constants as file_consts
import file_manager

router = APIRouter()


@router.on_event('startup')
async def prepare_uploading_dir():
    """Checks existence of uploading file dir and creates it if necessary."""
    if not os.path.isdir(file_consts.UPLOAD_DIR_NAME):
        os.mkdir(file_consts.UPLOAD_DIR_NAME)


@router.post(file_consts.UPLOAD_URL)
async def upload_file(file: UploadFile = File(...)):
    """Handles file uploading."""
    file_ext: str = file_manager.determine_file_ext(file.filename)
    if not file_ext:
        raise HTTPException(status_code=415, detail='Unknown file type')
    if file_ext not in file_consts.SUPPORTED_EXTENSIONS:
        raise HTTPException(status_code=415, detail='Invalid file type')
    file_was_successfully_saved: bool = await file_manager.save_file(file)
    if file_was_successfully_saved:
        return status.HTTP_200_OK
    else:
        raise HTTPException(status_code=415, detail='Too large file')
