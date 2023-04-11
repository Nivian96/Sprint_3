from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


def login(browser, registration):
    random_login, random_password = registration
    browser.get('https://stellarburgers.nomoreparties.site/login')

    login_input = browser.find_element(By.XPATH, './/form/fieldset[1]/div/div/input')
    password_input = browser.find_element(By.XPATH, './/form/fieldset[2]/div/div/input')
    submit_button = browser.find_element(By.XPATH, './/button[text()="Войти"]')

    login_input.send_keys(random_login)
    password_input.send_keys(random_password)
    submit_button.click()

    WebDriverWait(browser, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))
