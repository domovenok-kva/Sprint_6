from selenium.webdriver.common.by import By


class LocatorsForTest:

    @staticmethod
    def question_faq(q_index):
        return (By.XPATH, f'(//div[@class = "accordion__button"])[{q_index}]')
    
    @staticmethod
    def answer_faq(a_index):
        return (By.XPATH, f'(//div[@class = "accordion__panel"])[{a_index}]')
    
    faq_section = (By.CLASS_NAME, "Home_FAQ__3uVm4")

    order_button_header = (By.XPATH, "//div[contains(@class, 'Header_Nav')]/button[contains(@class, 'Button_Button')]")
    order_button_on_page = (By.XPATH, "//div[contains(@class, 'Home_FinishButton')]/button[contains(@class, 'Button_Button')]")
    name_input = (By.XPATH, "//input[contains(@placeholder, '* Имя')]")
    surname_input = (By.XPATH, "//input[contains(@placeholder, '* Фамилия')]")
    adress_input = (By.XPATH, "//input[contains(@placeholder, '* Адрес: куда привезти заказ')]")
    phone_number_input = (By.XPATH, "//input[contains(@placeholder, '* Телефон: на него позвонит курьер')]") 
    metro_select_search = (By.XPATH, "//input[contains(@placeholder, '* Станция метро')]")
    next_button = (By.XPATH, '//button[text() = "Далее"]')
    date_input = (By.XPATH, "//input[contains(@placeholder, '* Когда привезти самокат')]")
    calendar = (By.XPATH, "//div[contains(@class, 'react-datepicker__month-container')]")
    rental_term_dropdown = (By.XPATH, "//div[text()='* Срок аренды']")
    black_color_chbx = (By.XPATH, "//label[@for='black']")
    grey_color_chbx = (By.XPATH, "//label[@for='grey']")
    comment_input = (By.XPATH, "//input[contains(@placeholder, 'Комментарий для курьера')]")
    turnback_button = (By.XPATH, '//button[text() = "Назад"]')
    place_order_button  = (By.XPATH, '//div[contains(@class, "Order_Buttons__1xGrp")]/button[text() = "Заказать"]')
    yes_button  = (By.XPATH, '//button[text() = "Да"]')
    modal_window = (By.XPATH, '//div[contains(@class, "Order_Modal__YZ-d3")]')
    status_button = (By.XPATH, '//button[text() = "Посмотреть статус"]')
 
    scooter_logo = (By.XPATH, ".//a[@href='/']")
    yandex_logo = (By.XPATH, ".//a[@href='//yandex.ru']")
    
    @staticmethod
    def select_station(station: str):
        return (By.XPATH, f"//div[contains(text(),'{station}')]")
   
    @staticmethod
    def select_period(period: str):
        return (By.XPATH, f"//div[contains(text(),'{period}')]")

    @staticmethod
    def select_date(day_number: str):
        return (By.XPATH, f"//div[contains(text(),'{day_number}')]")

   