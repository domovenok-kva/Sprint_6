import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LocatorsForTest
from page_objects.base_page import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Жмяк на кнопку Заказать в Хедере')
    def click_order_btn_header(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.order_button_header)).click()

    @allure.step('Жмяк на кнопку Заказать в теле страницы')
    def click_order_btn_on_page(self):
        self.scroll_to_element(LocatorsForTest.order_button_on_page)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.order_button_on_page)).click()

