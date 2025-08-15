from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.devtools.v137.page import bring_to_front
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
import pytest
from time import sleep

@pytest.mark.skip('test skip')
def test_new_tab_open(browser):
    browser.get('https://www.qa-practice.com/elements/new_tab/link')
    browser.find_element(By.ID, 'new-page-link').click()
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    result = browser.find_element(By.ID, 'result-text')
    assert result.text == 'I am a new page in a new tab'

@pytest.mark.skip('test skip')
def test_switch_to_iframe(browser):
    browser.get('https://www.qa-practice.com/elements/iframe/iframe_page')
    iframe = browser.find_element(By.TAG_NAME, 'iframe')
    browser.switch_to.frame(iframe)
    burger_menu = browser.find_element(By.CLASS_NAME, 'navbar-toggler-icon')
    burger_menu.click()
    browser.switch_to.default_content()
    browser.find_element(By.LINK_TEXT, 'Homepage').click()

@pytest.mark.skip('test skip')
def test_switch_to_iframe_popup(browser):
    browser.get('https://www.qa-practice.com/elements/popup/modal')
    browser.find_element(By.LINK_TEXT, 'Iframe Pop-Up').click()
    browser.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary"]').click()
    iframe = browser.find_element(By.CSS_SELECTOR, 'iframe[class="embed-responsive-item"]')
    browser.switch_to.frame(iframe)
    TARGET_ELEMENT = (By.ID, 'text-to-copy')
    EXPECTED_TEXT = 'I am the text you want to copy'
    wait = WebDriverWait(browser, 10)
    text_element = wait.until(EC.visibility_of_element_located(TARGET_ELEMENT))
    assert text_element.text == EXPECTED_TEXT
    browser.switch_to.default_content()
    close_button = browser.find_element(By.CSS_SELECTOR, 'button[class="btn-close"]')
    close_button.click()

@pytest.mark.skip('test skip')
def test_open_menu_with_action_chains(browser):
    browser.get('https://practicum.yandex.ru/')
    about_practicum = browser.find_element(By.CLASS_NAME, 'submenu-arrow')
    testimonials = browser.find_element(By.XPATH, '//button[text()="Отзывы"]')
    actions = ActionChains(browser)
    actions.move_to_element(about_practicum)
    actions.click(testimonials)
    actions.perform()

@pytest.mark.skip('test skip')
def test_drag_and_drop(browser):
    browser.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_element = browser.find_element(By.ID, 'rect-draggable')
    drop_element = browser.find_element(By.ID, 'rect-droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(drag_element, drop_element)
    actions.perform()
    assert_text = (By.ID, 'text-droppable')
    wait = WebDriverWait(browser, 10)
    target_element = wait.until(EC.visibility_of_element_located(assert_text))
    assert target_element.text == "Dropped!"

@pytest.mark.skip('test skip')
def test_open_in_new_tab_with_control_key(browser):
    browser.get('https://www.qa-practice.com/elements/dragndrop/boxes')
    link = browser.find_element(By.LINK_TEXT, 'Homepage')
    actions = ActionChains(browser)
    actions.key_down(Keys.CONTROL)
    actions.click(link)
    actions.key_up(Keys.CONTROL)
    actions.perform()
    #======= Дополнительный блок =======
    tabs = browser.window_handles
    browser.switch_to.window(tabs[1])
    browser.switch_to.window(tabs[0])

@pytest.mark.skip('test skip')
def test_work_with_allert_just_assept(browser):
    browser.get('https://www.qa-practice.com/elements/alert/alert')
    button = browser.find_element(By.XPATH, '//a[contains(@onclick, "alert")]')
    button.click()
    alert = Alert(browser)
    alert.accept()

@pytest.mark.skip('test skip')
def test_work_with_allert_accept_or_cancel(browser):
    browser.get('https://www.qa-practice.com/elements/alert/alert')
    browser.find_element(By.XPATH, '//a[text()="Confirmation box"]').click()
    button = browser.find_element(By.XPATH, '//a[contains(@onclick, "if (confirm")]')
    button.click()
    allert = Alert(browser)
    allert.dismiss()


def test_work_with_allert_send_the_text_and_accept(browser):
    browser.get('https://www.qa-practice.com/elements/alert/alert')
    browser.find_element(By.XPATH, '//a[text()="Prompt box"]').click()
    button = browser.find_element(By.XPATH, '//a[contains(@onclick, "userText")]')
    button.click()
    allert = Alert(browser)
    allert.send_keys('Hello, bro!')
    allert.accept()



