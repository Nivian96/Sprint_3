from selenium.webdriver.common.by import By

from helpers import login


def test_transfer_to_fillings(browser, registration):
    login(browser, registration)
    browser.find_element(By.XPATH, './/span[text()="Начинки"]').click()

    assert browser.find_element(By.XPATH, './/h2[text()="Начинки"]').is_displayed()


def test_transfer_to_sauces(browser, registration):
    login(browser, registration)
    browser.find_element(By.XPATH, './/span[text()="Соусы"]').click()

    assert browser.find_element(By.XPATH, './/h2[text()="Соусы"]').is_displayed()


def test_transfer_to_rolls(browser, registration):
    login(browser, registration)
    browser.find_element(By.XPATH, './/span[text()="Соусы"]').click()
    browser.find_element(By.XPATH, './/span[text()="Булки"]').click()

    assert browser.find_element(By.XPATH, './/h2[text()="Булки"]').is_displayed()
