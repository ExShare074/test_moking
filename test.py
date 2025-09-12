import pytest
from main import get_weather
from config import WEATHER_API_KEY, CITY

def test_get_weather(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 25}
        }


    weather_data = get_weather(WEATHER_API_KEY, CITY)
    assert weather_data == {
        'weather': [{'description': 'clear sky'}],
        'main': {'temp': 25}
    }

def test_get_weather_with_error(mocker):
    mock_get = mocker.patch('main.requests.get')
    mock_get.return_value.status_code = 404

    weather_data = get_weather(WEATHER_API_KEY, CITY)
    assert weather_data == None