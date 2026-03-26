import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.locators import LocatorsForTest
from page_objects.base_page import BasePage

class FAQElements(BasePage):
    
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Скролл к FAQ")
    def scroll_to_faq(self):
        super().scroll_to_element(LocatorsForTest.faq_section)

    @allure.step("Выбор вопроса FAQ")
    def choose_faq_question(self, nmbr):
       self.scroll_to_faq()
       WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LocatorsForTest.question_faq(nmbr))).text
       WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LocatorsForTest.question_faq(nmbr))).click()
       return WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(LocatorsForTest.question_faq(nmbr))).text
        
    @allure.step("Получение ответа на вопрос")
    def get_faq_answer(self, nmbr):
        faq_answer = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(LocatorsForTest.answer_faq(nmbr)))
        return faq_answer.text 

