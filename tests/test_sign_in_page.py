# тесты для проверки регистрации
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from main import Generator
from locators import Locators

login = Generator.generate_login()
password = Generator.generate_password()

class TestSignIn():
    def test_incorrect_password(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")
        driver.find_element(By.XPATH, Locators.name_input).send_keys("UserName")
        driver.find_element(By.XPATH, Locators.email_input).send_keys(login)
        driver.find_element(By.XPATH, Locators.password_input).send_keys("1234")
        driver.find_element(By.XPATH, Locators.signin_button).click()
        incorrect_password = driver.find_element(By.CSS_SELECTOR, "p.input__error.text_type_main-default")
        assert "Некорректный пароль" == incorrect_password.text
        time.sleep(1)


    def test_sign_in_successful(self, driver):

        driver.get("https://stellarburgers.nomoreparties.site/register")
        user_name = driver.find_element(By.XPATH, Locators.name_input).send_keys("JamesBond")
        driver.find_element(By.XPATH, Locators.email_input).send_keys(login)
        driver.find_element(By.XPATH, Locators.password_input).send_keys(password)
        driver.find_element(By.XPATH, Locators.signin_button).click()

        assert len(password) >= 6  # проверка, что длина пароля >= 6 символам
        assert user_name != ""  # проверка, что поле Имя не пустое
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"  #после успешной регистрации попадаем на страницу логина
