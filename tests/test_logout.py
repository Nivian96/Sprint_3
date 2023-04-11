from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helpers import login


def test_logout(browser, registration):
    login(browser, registration)
    browser.find_element(By.XPATH, './/p[text()="Личный Кабинет"]').click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/a[text()="Профиль"]')))
    browser.find_element(By.XPATH, './/button[text()="Выход"]').click()
    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))

    assert browser.current_url == 'https://stellarburgers.nomoreparties.site/login'
