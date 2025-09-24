import pytest
from unittest.mock import patch, MagicMock
import requests
from printables_api import (
    search_models,
    get_real_download_url,
    get_model_files,
    get_model_description,
)

# Tests for search_models
@patch('printables_api.requests.post')
def test_search_models_success(mock_post):
    """
    Tests successful search functionality.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "result": {
                "items": [{"id": "123", "name": "Test Model"}]
            }
        }
    }
    mock_post.return_value = mock_response

    results = search_models("test", limit=1, ordering="best_match")
    assert len(results) == 1
    assert results[0]["name"] == "Test Model"
    mock_post.assert_called_once()

@patch('printables_api.requests.post')
def test_search_models_no_results(mock_post):
    """
    Tests search that returns no results.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "result": {
                "items": []
            }
        }
    }
    mock_post.return_value = mock_response

    results = search_models("something_that_doesnt_exist")
    assert len(results) == 0

def test_search_models_invalid_ordering():
    """
    Tests that an invalid ordering parameter raises a ValueError.
    """
    with pytest.raises(ValueError):
        search_models("test", ordering="invalid_ordering")

@patch('printables_api.requests.post')
def test_search_models_request_exception(mock_post):
    """
    Tests handling of a request exception.
    """
    mock_post.side_effect = requests.exceptions.RequestException("Test error")
    results = search_models("test")
    assert results == []

# Tests for get_real_download_url
@patch('printables_api.requests.post')
def test_get_real_download_url_success(mock_post):
    """
    Tests successfully getting a real download URL.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "getDownloadLink": {
                "ok": True,
                "output": {
                    "link": "https://example.com/download"
                }
            }
        }
    }
    mock_post.return_value = mock_response

    url = get_real_download_url("file1", "model1", "stl")
    assert url == "https://example.com/download"

@patch('printables_api.requests.post')
def test_get_real_download_url_failure(mock_post):
    """
    Tests failure to get a download URL.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "getDownloadLink": {
                "ok": False,
                "errors": [{"message": "Some error"}]
            }
        }
    }
    mock_post.return_value = mock_response

    url = get_real_download_url("file1", "model1", "stl")
    assert url is None

@patch('printables_api.requests.post')
def test_get_real_download_url_request_exception(mock_post):
    """
    Tests handling of a request exception.
    """
    mock_post.side_effect = requests.exceptions.RequestException("Test error")
    url = get_real_download_url("file1", "model1", "stl")
    assert url is None

# Tests for get_model_files
@patch('printables_api.get_real_download_url', return_value="https://example.com/download")
@patch('printables_api.requests.post')
def test_get_model_files_success(mock_post, mock_get_url):
    """
    Tests getting model files successfully.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "model": {
                "stls": [{"id": "stl1", "name": "part1.stl", "fileSize": 1024}],
                "gcodes": [{"id": "gcode1", "name": "part1.gcode", "fileSize": 2048}],
                "slas": [{"id": "sla1", "name": "part1.sla"}], # Unsupported
            }
        }
    }
    mock_post.return_value = mock_response

    files = get_model_files("model1")
    assert len(files) == 2
    assert files[0]['name'] == "part1.stl"
    assert files[1]['download_url'] == "https://example.com/download"
    assert mock_get_url.call_count == 2


@patch('printables_api.requests.post')
def test_get_model_files_no_files(mock_post):
    """
    Tests a model with no files.
    """
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = {
        "data": {
            "model": {}
        }
    }
    mock_post.return_value = mock_response

    files = get_model_files("model1")
    assert len(files) == 0

@patch('printables_api.requests.post')
def test_get_model_files_request_exception(mock_post):
    """
    Tests handling of a request exception.
    """
    mock_post.side_effect = requests.exceptions.RequestException("Test error")
    files = get_model_files("model1")
    assert files == []

# Tests for get_model_description
@patch('printables_api.cloudscraper.create_scraper')
def test_get_model_description_success(mock_create_scraper):
    """
    Tests successful scraping of a model description.
    """
    mock_scraper = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = '<html><body><div class="user-inserted"><h3>Title</h3><p>Description</p></div></body></html>'
    mock_scraper.get.return_value = mock_response
    mock_create_scraper.return_value = mock_scraper

    description = get_model_description("https://example.com/model")
    assert "## Title" in description
    assert "Description" in description

@patch('printables_api.cloudscraper.create_scraper')
def test_get_model_description_not_found(mock_create_scraper):
    """
    Tests when the description div is not found.
    """
    mock_scraper = MagicMock()
    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.text = '<html><body><div>No description here</div></body></html>'
    mock_scraper.get.return_value = mock_response
    mock_create_scraper.return_value = mock_scraper

    description = get_model_description("https://example.com/model")
    assert description == "Description not found on this page."

@patch('printables_api.cloudscraper.create_scraper')
def test_get_model_description_request_exception(mock_create_scraper):
    """
    Tests handling of a request exception.
    """
    mock_scraper = MagicMock()
    mock_scraper.get.side_effect = requests.exceptions.RequestException("Test error")
    mock_create_scraper.return_value = mock_scraper

    description = get_model_description("https://example.com/model")
    assert "Error: Could not fetch model page" in description