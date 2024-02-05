# Тест для проверки перехода в личный кабинет залогиненным юзером
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators
from selenium.webdriver.common.by import By

class TestPersonalAccount:
    def test_goto_personal_account(self, driver, loginfixture):

        driver.find_element(By.XPATH, Locators.personal_account_button).click()  # переходим в профиль,
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/account/profile"))
        assert driver.current_url == "https://stellarburgers.nomoreparties.site/account/profile"
