# Тест для проверки перехода из ЛК в Конструктор
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
class TestConstructor:
    def test_click_to_constructor(self, driver, loginfixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # переходим в профиль,
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        # перешли в профиль (ждем загрузку страницы)
        # чтобы потом проверить что по клику на Конструктор попадаем в нужный раздел

        driver.find_element(By.XPATH, Locators.constructor_button).click()  # клик на Конструктор
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        time.sleep(2)

    def test_click_to_logotype(self, driver, loginfixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # переходим в профиль,
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        # перешли в профиль (ждем загрузку страницы)
        # чтобы потом проверить что по клику на Конструктор попадаем в нужный раздел

        driver.find_element(By.XPATH, Locators.logotype_button).click()  # клик на лого
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
        time.sleep(2)