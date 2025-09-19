from http.client import responses

import pytest
import requests
import json


endpoint = 'https://fd2884d9-0c34-4185-b2e2-cbb7af6e64ff.serverhub.praktikum-services.ru/'

def test_get_all_kits():
    response = requests.get(f'{endpoint}' + 'api/v1/kits?cardId=1')
    assert response.status_code == 200
    print(' Успешно!')


def test_create_kit():
    body = {"name": "my_test_kit", "cardId": 3}
    response = requests.post(f'{endpoint}' + 'api/v1/kits', json = body)
    assert response

def test_delete_kit():
    response = requests.delete(f'{endpoint}' + f'api/v1/kits/3')
    assert response



