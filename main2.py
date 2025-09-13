# 1) Написать функцию, которая делает запрос к TheCatAPI для получения случайного изображения кошки.
# https://api.thecatapi.com/v1/images/search
#Написать тест, который проверяет успешный запрос и возвращает правильный URL.
#Написать тест, который проверяет неуспешный запрос (например, статус код 404) и возвращает None.
import requests

def get_api_cat():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None


