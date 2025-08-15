from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


# options = Options()
# options.add_argument('--start-maximized')
# #---- если есть необходимость в том, чтобы браузер не закрывался, прописываем эту опцию
# options.add_experimental_option('detach', True)

@pytest.mark.skip('later')
def test_link_text_and_css_selector(browser):
    browser.get('https://www.qa-practice.com/')
    target_row = browser.find_element(By.LINK_TEXT, 'Text input')
    target_row.click()
    row_for_assert = browser.find_element(By.CSS_SELECTOR, 'h1')
    assert row_for_assert.text == 'Input field'

@pytest.mark.skip('later')
def test_css_selector_and_send_keys(browser):
    browser.get('https://www.qa-practice.com/elements/input/simple')
    text_row = browser.find_element(By.CSS_SELECTOR, '.textinput')
    text_row.send_keys('TestMessage')
    text_row.submit()
    assert browser.find_element(By.CSS_SELECTOR, '.result-text').text == 'TestMessage'

@pytest.mark.skip('later')
def test_xpath(browser):
    browser.get('https://www.qa-practice.com/elements/input/simple')
    text_row = browser.find_element(By.XPATH, '//input[@name="text_string"]')
    text_row.send_keys('TestMessage')
    text_row.send_keys(Keys.ENTER)
    assert browser.find_element(By.XPATH, '//p[@id="result-text"]').text == 'TestMessage'

@pytest.mark.skip('later')
def test_placeholder(browser):
    browser.get('https://www.qa-practice.com/elements/input/simple')
    target_element = browser.find_element(By.CSS_SELECTOR, 'input[name="text_string"')
    assert target_element.get_attribute('placeholder') == 'Submit me'

@pytest.mark.skip('later')
def test_select(browser):
    browser.get('https://www.qa-practice.com/elements/button/disabled')
    button = browser.find_element(By.ID, 'submit-id-submit')
    print('------ Начало теста -------')
    print('Кнопка активна' if button.is_enabled() else 'Кнопка неактивна')
    select_row = browser.find_element(By.NAME, 'select_state')
    select_helper = Select(select_row)
    select_helper.select_by_value('enabled')
    print('---- Значение изменено ----')
    print('Кнопка активна' if button.is_enabled() else 'Кнопка неактивна')
    assert button.is_enabled()

def test_await_for_timer_is_over(browser):
    browser.get('https://practice-automation.com/javascript-delays/')
    start_button = browser.find_element(By.ID, 'start')
    start_button.click()
    wait = WebDriverWait(browser, 15)
    wait.until(EC.text_to_be_present_in_element((By.ID, 'delay'), 'Liftoff!'))
    assert 'Liftoff' in browser.find_element(By.ID, 'delay').text





