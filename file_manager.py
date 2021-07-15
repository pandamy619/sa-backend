import os

from fastapi import UploadFile

import constants


async def save_file(file: UploadFile):
    """Reads loaded to backend file and writes its content to new file."""
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
            return False
    new_file.close()
    return True


def determine_file_ext(file_name):
    """Determines file extension by file name."""
    if '.' not in file_name:
        return None
    ext = file_name.rsplit('.', maxsplit=1)[1]
    return ext
