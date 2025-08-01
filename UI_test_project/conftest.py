import requests
import pytest
import os
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('BASE_URL') # протухает через 2 часа, нужно обновлять
kits_endpoint = os.getenv('KITS_ENDPOINT')

@pytest.fixture()
def new_kit():
    body = {"name": "FixtureKit", "cardId": 10}
    response = requests.post(f'{base_url}{kits_endpoint}', json=body).json()
    kits_id = response['id']
    yield kits_id
    requests.delete(f'{base_url}{kits_endpoint}{kits_id}')