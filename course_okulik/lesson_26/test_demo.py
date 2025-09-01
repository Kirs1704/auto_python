from playwright.sync_api import Page, expect
import re
import pytest
from time import sleep

@pytest.mark.skip('Just skip')
def test_one(page: Page):
    page.goto('https://magento.softwaretestingboard.com')
    consent_button = page.get_by_role('button', name='Consent')
    consent_button.click()
    search_field = page.get_by_role('combobox')
    search_field.fill('Hero')
    page.keyboard.press('Enter')
    expect(page).to_have_url('https://magento.softwaretestingboard.com/catalogsearch/result/?q=Hero')

@pytest.mark.skip('Just skip')
def test_two(page: Page):
    page.goto('https://magento.softwaretestingboard.com')
    consent_button = page.get_by_role('button', name='Consent')
    consent_button.click()
    page.get_by_role('menuitem', name="What's New").click()
    page.get_by_role('link', name = 'Search Terms').click()
    expect(page).to_have_title('Popular Search Terms')

def test_by_text(page: Page):
    page.goto('https://qa-practice.com')
    page.get_by_text('Single UI Elements').click()

def test_by_label(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    text_string = page.get_by_label('Text string*')
    text_string.press_sequentially('HelloBro', delay=100)
    text_string.press('Control+a')
    text_string.press('Backspace')
    # assertion = page.get_by_role('paragraph')
    sleep(3)

def test_by_locator(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    page.locator('//*[@id="content"]/ul/li[2]/a').click()
    sleep(3)