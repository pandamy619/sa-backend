import os

from fastapi import FastAPI, File, UploadFile, status, HTTPException

import constants

app = FastAPI()


@app.on_event('startup')
async def init():
    """Checks existence of uploading file dir and creates it if necessary."""
    if not os.path.isdir(constants.UPLOAD_DIR_NAME):
        os.mkdir(constants.UPLOAD_DIR_NAME)


@app.post(constants.UPLOAD_URL)
async def upload_file(file: UploadFile = File(...)):
    """Handles file uploading."""
    if '.' not in file.filename:
        raise HTTPException(status_code=415, detail='Unknown file type')
    ext = file.filename.rsplit('.', maxsplit=1)[1]
    if ext not in constants.SUPPORTED_EXTENSIONS:
        raise HTTPException(status_code=415, detail='Invalid file type')
    new_file_name = os.path.join(constants.UPLOAD_DIR_NAME,
                                 file.filename)
    chunks_count = 0
    new_file = open(new_file_name, 'wb')
    while content := await file.read(constants.FILE_CHUNK_SIZE):
        new_file.write(content)
        chunks_count += 1
        if chunks_count > constants.CHUNKS_LIMIT:
            new_file.close()
            os.remove(new_file_name)
            raise HTTPException(status_code=415, detail='Too large file')
    new_file.close()
    return status.HTTP_200_OK
