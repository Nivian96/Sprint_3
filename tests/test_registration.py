import string
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def get_random_login():
    login = "viktoriya_vasyukova_08_" + "".join(random.choice(string.digits) for _ in range(3)) + "@yandex.ru"
    return login


def test_successful_registration(browser, random_password):
    login = get_random_login()
    browser.get('https://stellarburgers.nomoreparties.site/register')

    name_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    login_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/input[@type="password"]')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]')

    name_input.send_keys('Viktoriya')
    login_input.send_keys(login)
    password_input.send_keys(random_password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'


def test_invalid_password(browser, random_short_password):
    login = get_random_login()
    browser.get('https://stellarburgers.nomoreparties.site/register')

    name_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    login_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/input[@type="password"]')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]')

    name_input.send_keys('Viktoriya')
    login_input.send_keys(login)
    password_input.send_keys(random_short_password)
    submit_button.click()

    error_message = browser.find_element(By.CSS_SELECTOR, '.input__error')
    assert error_message.text == 'Некорректный пароль'
