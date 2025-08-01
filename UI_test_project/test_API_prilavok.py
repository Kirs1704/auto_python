import requests
import pytest
import os
import allure

# ======================== kits_api_tests. Positive cases =============================
base_url = os.getenv('BASE_URL') # протухает через 2 часа, нужно обновлять
kits_endpoint = os.getenv('KITS_ENDPOINT')


# Закоменченный блок с фикстурой вынесен в отдельный файл. См. conftest.py
# @pytest.fixture()
# def new_kit():
#     body = {"name": "FixtureKit", "cardId": 10}
#     response = requests.post(f'{BASE_URL}{KITS_ENDPOINT}', json=body).json()
#     kits_id = response['id']/
#     yield kits_id
#     requests.delete(f'{BASE_URL}{KITS_ENDPOINT}{kits_id}')

@allure.feature('Positive cases')
@allure.story('Create')
def test_create_new_kit():
    with allure.step('Prepare body for request'):
        body = {"name": "TestKit", "cardId": 44}
    with allure.step('Run POST request to create the kit'):
        response = requests.post(f'{base_url}{kits_endpoint}', json = body)
    with allure.step('Status code assertion'):
         assert response.status_code == 201, f'Not expecting status code {response.status_code}'
    with allure.step('Response conversion'):
        json_data = response.json()
        print(json_data)
    with allure.step('Check the "name" key is in response'):
        assert 'name' in json_data, 'Response must contain a "name" key'
    assert json_data['name'] == body['name'], 'Wrong key'
    assert 'productsList' in json_data, 'Response must contain a "productsList" key'
    assert json_data['productsList'] == None, 'Wrong value in "productList"'
    assert 'id' in json_data, 'Response must contain a "id" key'
    assert isinstance(json_data['id'], (int)), '"id" must be an integer'
    #print(f'\n{json_data}')

@allure.feature('Positive cases')
@allure.story('Add')
def test_add_product_to_kit(new_kit):
    body = {"productsList": [{"id": 1,"quantity": 1}]}
    response = requests.post(f'{base_url}{kits_endpoint}{new_kit}/products', json = body)
    assert response.status_code == 200, f'Expecting status_code 200, getting {response.status_code}'
    json_data = response.json()
    assert 'productsList' in json_data, 'Expecting key "products" in response body'
    assert json_data['productsList'][0]['id'] == body['productsList'][0]['id'], 'Wrong items in productsList'

# ======================== kits_api_tests. Negative cases =============================
@allure.feature('Negative cases')
def test_create_kit_without_name_error_expected():
    body = {}
    response = requests.post(f'{base_url}{kits_endpoint}', json=body)
    assert response.status_code == 400, f'Expected status code "400", but {response.status_code} returned'
    json_data = response.json()
    assert 'message' in json_data, 'Expected key "message", but it is not present'
    assert json_data['message'] == 'Не все необходимые параметры были переданы', 'Wrong message'

# ======================== kits_api_tests. Advanced cases =============================
@allure.feature('Advanced cases')
@pytest.mark.parametrize('kit_names', [' ', '%', 1])
def test_create_kit_with_different_names(kit_names):
    body = {"name": kit_names, "cardId": 44}
    response = requests.post(f'{base_url}{kits_endpoint}', json=body)
    assert response.status_code == 201, f'Expected status code "201", but {response.status_code} returned'
    json_data = response.json()
    assert 'name' in json_data
    assert json_data['name'] == body['name']








