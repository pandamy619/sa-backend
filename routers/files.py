from fastapi import File, UploadFile, status, HTTPException, APIRouter

import file_related.constants as file_consts
import file_related.functions as file_functions

router = APIRouter()


@router.post(file_consts.UPLOAD_URL)
async def upload_file(file: UploadFile = File(...)) -> int:
    """Handles file uploading."""
    file_ext: str = file_functions.determine_file_ext(file.filename)
    if not file_ext:
        raise HTTPException(status_code=415, detail='Unknown file type')
    if file_ext not in file_consts.SUPPORTED_EXTENSIONS:
        raise HTTPException(status_code=415, detail='Invalid file type')
    file_was_successfully_saved: bool = await file_functions.save_file(file)
    if file_was_successfully_saved:
        return status.HTTP_200_OK
    else:
        raise HTTPException(status_code=415, detail='Too large file')
