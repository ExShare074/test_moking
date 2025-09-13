import pytest
from main2 import get_api_cat

def test_get_api_cat(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [
        {'url': 'https://example.com/cat.jpg'}
    ]

    user_data = get_api_cat()
    assert user_data[0]['url'] == 'https://example.com/cat.jpg'


def test_get_api_cat_error(mocker):
    mock_get = mocker.patch('requests.get')
    mock_get.return_value.status_code = 404

    user_data = get_api_cat()
    assert user_data is None