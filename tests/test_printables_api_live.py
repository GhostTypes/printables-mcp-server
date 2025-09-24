import pytest
from printables_api import get_model_description, get_model_files, get_real_download_url

LIVE_TEST_URL = "https://www.printables.com/model/3161-3d-benchy"
LIVE_TEST_MODEL_ID = "3161"
# From the previous run, we know the file ID for 3dbenchy.stl is 49068, but we will get it dynamically
LIVE_TEST_FILE_ID = "49068"


@pytest.mark.live
def test_get_model_description_live():
    """
    Tests get_model_description with a live URL.
    """
    description = get_model_description(LIVE_TEST_URL)
    assert "3D model specifically designed for testing and benchmarking 3D printers" in description

@pytest.mark.live
def test_get_model_files_live():
    """
    Tests get_model_files with a live model ID.
    """
    files = get_model_files(LIVE_TEST_MODEL_ID)
    assert len(files) > 0
    assert any(f['name'] == '3dbenchy.stl' for f in files)

@pytest.mark.live
def test_get_real_download_url_live():
    """
    Tests get_real_download_url with a live file ID.
    """
    url = get_real_download_url(LIVE_TEST_FILE_ID, LIVE_TEST_MODEL_ID, "stl")
    assert url is not None
    assert "https://files.printables.com/" in url