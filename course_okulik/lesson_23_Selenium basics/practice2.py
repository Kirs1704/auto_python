from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pytest

from course_okulik.lesson_16.creds import passwd


@pytest.fixture()
def browser():
    options = Options()
    options.add_argument('--start-maximized')
    #options.add_experimental_option('detach', True)
    driver = webdriver.Chrome(options=options)
    return driver

def test_find_element_with_id(browser):
    input_data = 'Test123'
    browser.get('https://www.qa-practice.com/')
    browser.find_element(By.LINK_TEXT, 'Text input').click()
    browser.find_element(By.ID, 'caret-down').click()
    submit_row = browser.find_element(By.ID, 'id_text_string')
    submit_row.send_keys(input_data)
    # submit_row.submit()
    submit_row.send_keys(Keys.ENTER)
    result_text = browser.find_element(By.ID, 'result-text')
    assert result_text.text == input_data


