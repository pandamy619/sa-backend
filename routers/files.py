import os

from fastapi import File, UploadFile, status, HTTPException, APIRouter

import constants
import file_manager

router = APIRouter()


@router.on_event('startup')
async def init():
    """Checks existence of uploading file dir and creates it if necessary."""
    if not os.path.isdir(constants.UPLOAD_DIR_NAME):
        os.mkdir(constants.UPLOAD_DIR_NAME)


@router.post(constants.UPLOAD_URL)
async def upload_file(file: UploadFile = File(...)):
    """Handles file uploading."""
    file_ext = file_manager.determine_file_ext(file.filename)
    if not file_ext:
        raise HTTPException(status_code=415, detail='Unknown file type')
    if file_ext not in constants.SUPPORTED_EXTENSIONS:
        raise HTTPException(status_code=415, detail='Invalid file type')
    successfully_written = await file_manager.save_file(file)
    if successfully_written:
        return status.HTTP_200_OK
    else:
        raise HTTPException(status_code=415, detail='Too large file')
