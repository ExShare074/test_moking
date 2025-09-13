import pytest
from main import get_github_user

def test_get_github_user(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'login': 'ValeraGigachat',
        'id': 123456,
        'name': 'Valera'
    }

    user_data = get_github_user('ValeraGigachat')
    assert user_data == {
        'login': 'ValeraGigachat',
        'id': 123456,
        'name': 'Valera'
    }


def test_get_github_user_invalid(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 500


    user_data = get_github_user('ValeraGigachat')
    assert user_data == None
