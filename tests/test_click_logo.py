import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from page_objects.home_page import HomePage
from page_objects.order_page import OrderElements
from locators.locators import LocatorsForTest

class TestLogo:
    @allure.title('Переход по лого Самоката')
    def test_scooter_logo(self, driver):
        h_page = HomePage(driver)
        h_page.click_order_btn_header()
        o_page = OrderElements(driver)
        o_page.click_scooter_logo()
        assert WebDriverWait(driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.order_button_on_page)).is_displayed()

    @allure.title('Переход по лого Яндекса')
    def test_ya_logo(self, driver):
        h_page = HomePage(driver)
        h_page.click_order_btn_header()
        o_page = OrderElements(driver)
        o_page.click_ya_logo()
        dzen = 'https://dzen.ru/?yredirect=true'
        driver.switch_to.window(driver.window_handles[1])
        WebDriverWait(driver, 5).until(EC.url_to_be(dzen))
        assert driver.current_url == dzen

