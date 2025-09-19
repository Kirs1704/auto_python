from time import sleep

from playwright.sync_api import Page, expect, BrowserContext, Dialog
import re

# ЭЛЕМЕНТ ВИДЕН НА СТРАНИЦЕ
def test_is_element_visible(page: Page):
    page.goto('https://www.qa-practice.com/elements/input/simple')
    target_element = page.locator('//div[@class="card card-body"]')
    expect(target_element).to_be_hidden()
    page.get_by_role('button', name='Requirements').click()
    expect(target_element).to_be_visible()

# ЭЛЕМЕНТ АКТИВЕН И ВЫБРАН
def test_enabled_and_selected(page: Page):
    page.goto('https://www.qa-practice.com/elements/button/disabled')
    submit_button = page.get_by_role('button', name='Submit')
    expect(submit_button).to_be_disabled()
    page.get_by_role('combobox').select_option('Enabled')
    expect(submit_button).to_be_enabled()
    submit_button.click()
    target_element_for_assert = page.locator('#result-text')
    expect(target_element_for_assert).to_have_text('Submitted')

# ПРОВЕРКА НАЛИЧИЯ ЗНАЧЕНИЯ У ЭЛЕМЕНТА
def test_contain_value(page: Page):
    test_text = 'Hello'
    page.goto('https://www.qa-practice.com/elements/input/simple')
    input_field = page.locator('#id_text_string')
    input_field.fill('Hello')
    expect(input_field, f'Value should be a "{test_text}", but didn\'t get it').to_have_value(test_text)

# СОРТИРОВКА ТОВАРОВ НА СТРАНИЦЕ
def test_sort(page: Page):
    page.goto('https://magento.softwaretestingboard.com/men/tops-men/jackets-men.html')
    consent_button = page.get_by_role('button', name='Consent')
    consent_button.click()
    first_man = page.locator('.product-item-link').locator('nth=0')
    print(first_man.inner_text())
    page.get_by_role('combobox', name='Sort By').select_option('Price')
    print(first_man.inner_text())

# ЭЛЕМЕНТ В ФОКУСЕ
def test_element_in_focus(page: Page):
    page.goto('https://www.google.com')
    accept_message = page.locator('//button[@id="L2AGLb"]/div[contains(text(), "Принять все")]')
    expect(accept_message).to_be_visible()
    accept_message.click()
    target_element = page.locator('#APjFqb')
    expect(target_element).not_to_be_focused()
    target_element.click()
    expect(target_element).to_be_focused()

# РАБОТА С ТАБАМИ
def test_tubs(page: Page, context: BrowserContext):
    test_data = 'I am a new page in a new tab'
    page.goto('https://www.qa-practice.com/elements/new_tab/link')
    link = page.locator('#new-page-link')
    with context.expect_page() as new_page_event:
        link.click()
    new_page = new_page_event.value
    target_element = new_page.locator('#result-text')
    expect(target_element).to_be_visible()
    expect(target_element).to_have_text('I am a new page in a new tab')

# НАВЕДЕНИЕ НА ЭЛЕМЕНТ
def test_hover(page: Page):
    page.goto('https://magento.softwaretestingboard.com')
    consent_button = page.get_by_role('button', name='Consent')
    consent_button.click()
    men = page.locator('#ui-id-5')
    tops = page.locator('#ui-id-17')
    jackets = page.locator('#ui-id-19')
    men.hover()
    tops.hover()
    jackets.click()
    sleep(3)

# Drag-n-Drop. Перетягивание
def test_d_n_d(page: Page):
    page.goto('https://www.qa-practice.com/elements/dragndrop/boxes')
    drag_me_element = page.locator('#rect-draggable')
    drop_here_element = page.locator('#text-droppable')
    drag_me_element.drag_to(drop_here_element)
    sleep(3)

# РАБОТА С АЛЕРТАМИ
def test_alert(page: Page):
    def fill_and_accept(alert: Dialog):
        alert.accept('Hello!')

    def cancel_alert(alert: Dialog):
        print(alert.message)
        print(alert.type)
        alert.dismiss()

    page.on('dialog', cancel_alert) # Включаем отслеживание алертов (диалогов по Плэйрайтовски) и указываем действие
    page.goto('https://www.qa-practice.com/elements/alert/alert')
    page.get_by_role('link', name='Click').click()
