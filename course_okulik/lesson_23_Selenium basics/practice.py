from selenium.webdriver.common.by import By


def test_successful_registration_and_login(browser, fake_data_for_test):
    browser.get('http://users.bugred.ru/')
    name, email, password = fake_data_for_test
    browser.find_element(By.LINK_TEXT,  'Войти').click()
    name_input = browser.find_element(By.NAME, 'name')
    name_input.send_keys(name)
    email_input = browser.find_element(By.NAME, 'email')
    email_input.send_keys(email)
    pass_input = browser.find_element(By.XPATH, '/html/body/div[3]/div[1]/div[2]/form/table/tbody/tr[3]/td[2]/input')
    pass_input.send_keys(password)
    browser.find_element(By.NAME, 'act_register_now').click()
    target_el = browser.find_element(By.LINK_TEXT, 'Задачи')
    assert target_el.text == 'Задачи'

