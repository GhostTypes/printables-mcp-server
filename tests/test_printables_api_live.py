import pytest
from printables_api import get_model_description, get_model_files

LIVE_TEST_URL = "https://www.printables.com/model/3161-3d-benchy"
LIVE_TEST_MODEL_ID = "3161"

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