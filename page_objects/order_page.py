import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LocatorsForTest
from page_objects.home_page import HomePage

class OrderElements(HomePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Заполнение поля Имя')
    def fill_in_name_inpt(self, name):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.name_input)).send_keys(name)

    @allure.step('Заполнение поля Фамилия')
    def fill_in_surname_inpt(self, surname):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.surname_input)).send_keys(surname)
    
    @allure.step('Заполнение поля Адрес')
    def fill_in_adress_inpt(self, adress):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.adress_input)).send_keys(adress)

    @allure.step('Заполнение поля Станция Метро')
    def fill_in_metro(self, metro_stantion):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.metro_select_search)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.metro_select_search)).send_keys(metro_stantion)
        self.find_element(LocatorsForTest.select_station(metro_stantion)).click()

    @allure.step('Заполнение поля Номер телефона')
    def fill_in_ph_number(self, number):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.phone_number_input)).send_keys(number)

    @allure.step('Нажатие на кнопку Далее')
    def click_next_btn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.next_button)).click()

    @allure.step('Выбор даты доставки')
    def choose_date(self, delivery_date):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.date_input)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.date_input)).send_keys(delivery_date)
        self.find_element(LocatorsForTest.select_date(delivery_date)).click()
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.calendar)).click()

    @allure.step('Выбор срока аренды')
    def choose_rent_term(self, rent_period):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.rental_term_dropdown)).click()
        self.find_element(LocatorsForTest.select_period(rent_period)).click()

    @allure.step('Выбор цвета самоката')
    def choose_scooter_colour(self, colour):
        if colour == 'чёрный жемчуг':
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.black_color_chbx)).click()
        elif colour == 'серая безысходность':
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.grey_color_chbx)).click()       

    @allure.step('Ввод коммента')
    def fill_in_comment(self, comment):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.comment_input)).send_keys(comment)

    @allure.step('Нажатие на кнопку Заказать')
    def click_place_order_bttn(self):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.place_order_button)).click()
    

    @allure.step('Заказ')
    def place_an_order(self, name, surname, adress, metro_stantion, number, delivery_date, rent_period, colour, comment):
        self.fill_in_name_inpt(name)
        self.fill_in_surname_inpt(surname)
        self.fill_in_adress_inpt(adress)
        self.fill_in_metro(metro_stantion)
        self.fill_in_ph_number(number)
        self.click_next_btn()
        self.choose_date(delivery_date)
        self.choose_rent_term(rent_period)
        self.choose_scooter_colour(colour)
        self.fill_in_comment(comment)
        self.click_place_order_bttn()

    @allure.step('Клик по лого Яндекса')
    def click_ya_logo(self):
        self.find_element(LocatorsForTest.yandex_logo).click()

    @allure.step('Клик по лого Самоката')
    def click_scooter_logo(self):
        self.find_element(LocatorsForTest.scooter_logo).click()

