# Страница раздела Местоположение
import allure
from selenium.webdriver.common.by import By
from base.seleniumbase import SeleniumBase


@allure.epic("Location Page")
class LocationPage(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self._page_title = (By.XPATH, "//h1")

    @allure.step("Получение текста заголовка страницы")
    def get_page_title_text(self):
        return self.driver.find_element(*self._page_title).text
