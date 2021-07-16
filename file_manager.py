import os

from fastapi import UploadFile

from routers.file_constants import UPLOAD_DIR_NAME

# 1 MB.
FILE_CHUNK_SIZE = 1048576
CHUNKS_LIMIT = 300


async def save_file(file: UploadFile) -> bool:
    """Reads loaded to backend file and writes its content to new file."""
    new_file_name = os.path.join(UPLOAD_DIR_NAME, file.filename)
    chunks_count = 0
    new_file = open(new_file_name, 'wb')
    while content := await file.read(FILE_CHUNK_SIZE):
        new_file.write(content)
        chunks_count += 1
        if chunks_count > CHUNKS_LIMIT:
            new_file.close()
            os.remove(new_file_name)
            return False
    new_file.close()
    return True


def determine_file_ext(file_name: str) -> str:
    """Determines file extension by file name."""
    if '.' not in file_name:
        return None
    ext = file_name.rsplit('.', maxsplit=1)[1]
    return ext
