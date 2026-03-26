import allure
import pytest
from testdata.testdata import  ClientData
from page_objects.home_page import HomePage
from page_objects.order_page import OrderElements
from locators.locators import LocatorsForTest

class TestOrder:
    
     @allure.title('Проверка заказа из хедера')
     def test_click_order_btn_header(self, driver):
          h_page = HomePage(driver)
          h_page.click_order_btn_header()
          o_page = OrderElements(driver)
          assert  o_page.find_element(LocatorsForTest.next_button)
          
          
     @allure.title('Проверка заказа из тела')
     def test_click_order_button_on_page(self, driver):
          h_page = HomePage(driver)
          h_page.click_order_btn_on_page()
          o_page = OrderElements(driver)
          assert  o_page.find_element(LocatorsForTest.next_button)

     @allure.title('Заказ самоката, 2 варианта')
     @pytest.mark.parametrize(ClientData.values, ClientData.ClientOne)
     def test_full_scooter_order(self, driver, name, surname, adress, metro_stantion, number, delivery_date, rent_period, colour, comment):
          h_page = HomePage(driver)
          h_page.click_order_btn_header()
          o_page = OrderElements(driver)
          o_page.place_an_order(name, surname, adress, metro_stantion, number, delivery_date, rent_period, colour, comment)
          assert o_page.find_element(LocatorsForTest.modal_window) 

     