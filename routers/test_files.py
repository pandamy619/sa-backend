import enum
import os

from fastapi.testclient import TestClient

from file_related.constants import UPLOAD_URL, UPLOAD_DIR_NAME
from main import main as create_app

TESTING_FILES_DIR = os.path.join('file_related', 'testing_uploads')
app = create_app()
client = TestClient(app)


class FileName(enum.Enum):
    """Files used during testing."""

    OK_CSV = 'test.csv'
    OK_XLS = 'test.xls'
    OK_XLSX = 'test.xlsx'
    UNKNOWN_TYPE = 'unknown type'
    INVALID_TYPE = 'invalid type.txt'


def _test_valid_file_uploading(file_name: str):
    """Checks that API returns status 200 and saves uploaded file."""
    with open(os.path.join(TESTING_FILES_DIR, file_name), 'rb') as upld_file:
        files = {'file': upld_file}
        response = client.post(UPLOAD_URL, files=files)
        assert response.status_code == 200
        local_file_name = os.path.join(UPLOAD_DIR_NAME, file_name)
        assert os.path.exists(local_file_name)
        os.remove(local_file_name)


def test_upload_file_success_csv():
    """Tests correct .csv file uploading."""
    _test_valid_file_uploading(FileName.OK_CSV.value)


def test_upload_file_success_xls():
    """Tests correct .xls file uploading."""
    _test_valid_file_uploading(FileName.OK_XLS.value)


def test_upload_file_success_xlsx():
    """Tests correct .xlsx file uploading."""
    _test_valid_file_uploading(FileName.OK_XLSX.value)


def test_unknown_file_type():
    """Checks that API returns status 415 for file without extension."""
    file_name = os.path.join(TESTING_FILES_DIR, FileName.UNKNOWN_TYPE.value)
    with open(file_name, 'rb') as up_file:
        files = {'file': up_file}
        response = client.post(UPLOAD_URL, files=files)
        assert response.status_code == 415
        local_file_name = os.path.join(UPLOAD_DIR_NAME, file_name)
        assert not os.path.exists(local_file_name)


def test_invalid_file_type():
    """Checks that API returns status 415 for unsupported file uploaoding."""
    file_name = os.path.join(TESTING_FILES_DIR, FileName.INVALID_TYPE.value)
    with open(file_name, 'rb') as up_file:
        files = {'file': up_file}
        response = client.post(UPLOAD_URL, files=files)
        assert response.status_code == 415
        local_file_name = os.path.join(UPLOAD_DIR_NAME,
                                       FileName.INVALID_TYPE.value)
        assert not os.path.exists(local_file_name)
