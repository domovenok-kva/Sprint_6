import allure
import pytest
from testdata.testdata import FAQData
from page_objects.faq_page import FAQElements

class TestFAQ:
    @allure.title('Проверка FAQ')
    @pytest.mark.parametrize('number, question, answer', FAQData.correct_answer)
    def test_pick_faq(self, driver, number, question, answer):
        faq_elements = FAQElements(driver)
        question_contains =  faq_elements.choose_faq_question(number)
        faq_elements.choose_faq_question(number)
        answer_contains =  faq_elements.get_faq_answer(number)
        assert question_contains == question
        assert answer_contains  == answer
        