from faker import Faker
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--start-maximized')
    # options.add_experimental_option('detach', True)
    chrome_driver = webdriver.Chrome(options = options)
    # Добавляет неявное ожидание (можно использовать если нужно "общее" ожидание)
    #chrome_driver.implicitly_wait(5)
    return chrome_driver

@pytest.fixture()
def fake_data_for_test():
    fake = Faker()
    name = fake.first_name()
    email = fake.email()
    password = fake.password()
    return name, email, password