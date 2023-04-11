from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import login


def test_transfer_to_constructor(browser, registration):
    login(browser, registration)
    browser.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()
    browser.find_element(By.XPATH, './/p[text()="Конструктор"]').click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'


def test_transfer_to_constructor_by_logo(browser, registration):
    login(browser, registration)
    browser.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()
    browser.find_element(By.XPATH, './/header/nav/div/a').click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h1[text()="Соберите бургер"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/'
