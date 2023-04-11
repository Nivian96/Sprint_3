import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture()
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def random_login():
    login = "viktoriya_vasyukova_08_" + "".join(random.choice(string.digits) for _ in range(3)) + "@yandex.ru"
    return login


@pytest.fixture(scope="session")
def random_password():
    password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    return password


@pytest.fixture()
def random_short_password():
    short_password = "".join(random.choice(string.ascii_letters + string.digits) for _ in range(5))
    return short_password


@pytest.fixture(scope="session")
def registration(random_login, random_password):
    browser = webdriver.Chrome()
    browser.get('https://stellarburgers.nomoreparties.site/register')

    name_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    login_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/input[@type="password"]')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Зарегистрироваться"]')

    name_input.send_keys('Viktoriya')
    login_input.send_keys(random_login)
    password_input.send_keys(random_password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))
    browser.quit()
    return random_login, random_password
