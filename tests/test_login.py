from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def test_login_via_login_account_button_on_homepage(browser, registration):
    login, password = registration
    browser.get('https://stellarburgers.nomoreparties.site/')

    login_button = browser.find_element(By.XPATH, './/button[text()="Войти в аккаунт"]')
    login_button.click()

    login_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Войти"]')

    login_input.send_keys(login)
    password_input.send_keys(password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_login_via_personal_account_button(browser, registration):
    login, password = registration
    browser.get('https://stellarburgers.nomoreparties.site/')

    personal_account_button = browser.find_element(By.XPATH, './/p[text()="Личный Кабинет"]')
    personal_account_button.click()

    login_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Войти"]')

    login_input.send_keys(login)
    password_input.send_keys(password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_login_via_registration_form_button(browser, registration):
    login, password = registration
    browser.get('https://stellarburgers.nomoreparties.site/register')

    personal_account_button = browser.find_element(By.XPATH, './/a[text()="Войти"]')
    personal_account_button.click()

    login_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Войти"]')

    login_input.send_keys(login)
    password_input.send_keys(password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_login_via_password_recovery_form_button(browser, registration):
    login, password = registration
    browser.get('https://stellarburgers.nomoreparties.site/forgot-password')

    personal_account_button = browser.find_element(By.XPATH, './/a[text()="Войти"]')
    personal_account_button.click()

    login_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Войти"]')

    login_input.send_keys(login)
    password_input.send_keys(password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'
