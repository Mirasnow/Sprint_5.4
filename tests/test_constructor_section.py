# Тест для проверки переходов по разделам Конструктора
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

class TestConstructorSection:
    def test_click_to_section(self, driver, loginfixture):

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_sauce).click()  # переходим в раздел "Соусы" с задержкой 3с для наглядности
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.constructor_topping).click()  # переходим в раздел "Начинки" с задержкой 3с для наглядности
        time.sleep(1)
        driver.find_element(By.XPATH, Locators.constructor_bread).click()  # переходим в раздел "Булки" с задержкой 3с для наглядности
        time.sleep(1)
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/"
