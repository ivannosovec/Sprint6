import os
import sys
from pages.base_page import *
from pages.main_page import *
import pytest
import allure
from data import *

class MainPage(BasePage):
    @allure.title('Проверка перехода к оформлению заказа по кнопке "Заказать')
    @allure.description('Тестирование перехода на страницу оформления заказа при клике на кнопку заказать в хедере '
                        'или на главной странице')
    @pytest.mark.parametrize('order_button', [
        MainPageLocators.order_button_in_header,
        MainPageLocators.order_button_in_page
    ])
    def test_move_to_order_page(self, order_button, start_from_main_page):
        main_page = MainPage(start_from_main_page)
        main_page.click_order_button(order_button)
        assert main_page.get_current_url() == order_url

    @allure.title('Проверка вопросов и ответов в секции "Вопросы о важном"')
    @allure.description('Тестирование того, что при клике на вопрос в секции "Вопросы о важном" отображается '
                        'соответствующий ему ответ')
    @pytest.mark.parametrize('question_number, expected_answer', TestData.test_data_question_answers)
    def test_click_on_faq_question_open_right_answer(self, question_number, expected_answer, start_from_main_page):
        main_page = MainPage(start_from_main_page)
        assert main_page.get_faq_question_answer_text(question_number) == expected_answer
    