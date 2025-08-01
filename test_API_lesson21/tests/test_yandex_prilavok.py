import allure
from test_API_lesson21.endpoints.create_kit import CreateKit

@allure.feature('Positive cases')
@allure.story('Create')
def test_create_new_kit():
    body = {"name": "TestKit", "cardId": 44}
    kit_client = CreateKit()
    response = kit_client.post_create_new_kit(body)
    assert response.status_code == 201, f'Not expecting status code {response.status_code}'
    json_data = response.json()
    assert 'name' in json_data, 'Response must contain a "name" key'
    assert json_data['name'] == body['name'], 'Wrong key'
    assert 'productsList' in json_data, 'Response must contain a "productsList" key'
    assert json_data['productsList'] is None, 'Wrong value in "productList"'
    assert 'id' in json_data, 'Response must contain a "id" key'
    assert isinstance(json_data['id'], (int)), '"id" must be an integer'