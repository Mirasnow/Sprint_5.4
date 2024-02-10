# тесты для проверки Выхода (разлогина)
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestLogout:
    def test_logout(self, driver, loginfixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # переходим в профиль
        logout = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, Locators.logout_button)))  # ждем пока кнопка "Выход" станет кликабельной
        logout.click()  # клик на "Выход"
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/login"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/login"
