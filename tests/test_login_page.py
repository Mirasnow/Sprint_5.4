# тесты для проверки Входа
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLogin:
    # Вход по кнопке "Войти в аккаунт"
    def test_login_to_account_button(self, driver, loginfixture):

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    # Вход по кнопке "Личный кабинет"
    def test_login_persona_account_button(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/")
        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # клик по кнопке "Личный кабинет"
        driver.find_element(By.XPATH, Locators.email_input).send_keys("elmirafyaizullina5432@yandex.ru")
        driver.find_element(By.XPATH, Locators.password_input).send_keys("123456")
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    # Вход на странице Регистрации
    def test_login_signin_page(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, Locators.login_button).click()  # клик по кнопке "Войти" на странице регистрации
        driver.find_element(By.XPATH, Locators.email_input).send_keys("elmirafyaizullina5432@yandex.ru")
        driver.find_element(By.XPATH, Locators.password_input).send_keys("123456")
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"


    # Вход на странице Восстановления пароля
    def test_login_password_recovery_page(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/forgot-password")
        driver.find_element(By.XPATH, Locators.login_button).click()  # клик по кнопке "Войти" на странице восстановления пароля
        driver.find_element(By.XPATH, Locators.email_input).send_keys("elmirafyaizullina5432@yandex.ru")
        driver.find_element(By.XPATH, Locators.password_input).send_keys("123456")
        driver.find_element(By.XPATH, Locators.enter_button).click()
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
