import allure
from page_objects.home_page import HomePage
from page_objects.order_page import OrderElements
from locators.locators import LocatorsForTest
from testdata.testdata import MyURLS

class TestLogo:
    @allure.title('Переход по лого Самоката')
    def test_scooter_logo(self, driver):
        h_page = HomePage(driver)
        h_page.click_order_btn_header()
        o_page = OrderElements(driver)
        o_page.click_scooter_logo()
        assert o_page.find_element(LocatorsForTest.order_button_on_page)

    @allure.title('Переход по лого Яндекса')
    def test_ya_logo(self, driver):
        h_page = HomePage(driver)
        h_page.click_order_btn_header()
        o_page = OrderElements(driver)
        o_page.click_ya_logo()
        driver.switch_to.window(driver.window_handles[1])
        o_page.wait_for_page(driver)
        assert driver.current_url == MyURLS.dzen_url

