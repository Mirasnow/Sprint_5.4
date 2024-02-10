# Тест для проверки переходов по разделам Конструктора
from locators import Locators
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class TestConstructorSection:
    def test_click_to_section_sauce(self, driver, loginfixture):

        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_sauce).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.selected_sauce)))
        current_tab = driver.find_element(By.XPATH,Locators.selected_sauce)
        assert current_tab.is_displayed()

    def test_click_to_section_topping(self, driver, loginfixture):
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_topping).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.selected_topping)))
        current_tab = driver.find_element(By.XPATH,Locators.selected_topping)
        assert current_tab.is_displayed()

    def test_click_to_section_bread(self, driver, loginfixture):
        WebDriverWait(driver, 10).until(EC.url_to_be("https://stellarburgers.nomoreparties.site/"))
        driver.find_element(By.XPATH, Locators.constructor_topping).click()
        driver.find_element(By.XPATH, Locators.constructor_bread).click()
        WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, Locators.selected_bread)))
        current_tab = driver.find_element(By.XPATH,Locators.selected_bread)
        assert current_tab.is_displayed()
