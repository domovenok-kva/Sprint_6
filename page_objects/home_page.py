import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LocatorsForTest

class HomePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    def find_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Скролл')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Жмяк на кнопку Заказать в Хедере')
    def click_order_btn_header(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.order_button_header)).click()

    @allure.step('Жмяк на кнопку Заказать в теле страницы')
    def click_order_btn_on_page(self):
        self.scroll_to_element(LocatorsForTest.order_button_on_page)
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.order_button_on_page)).click()

   
        

  
