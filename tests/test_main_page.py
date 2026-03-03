import os
import sys
directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(directory)
sys.path.append(directory + '\\pages')
from pages.base_page import *
from pages.main_page import *
import pytest
import allure
from data import *

class TestMainPageQuestions:
    @allure.title('Проверка показа ответов в разделе "Вопросы о важном"')
    @allure.description('Проверяем вопрос: кликаем, убеждаемся, что нужный ответ развернулся')
    @pytest.mark.parametrize('question_id', [0, 1, 2, 3, 4, 5, 6, 7])
    def test_answer_is_displayed_when_arrow_clicked(self, driver, question_id):
        main_page=MainPageSamokat(driver)
        main_page.scroll_to_quest_arrow(question_id)
        main_page.click_quest_arrow(question_id)
        assert main_page.check_quest_answer_displayed(question_id)

    @allure.title('Проверка соответствия ответов в разделе "Вопросы о важном"')
    @allure.description('Проверяем вопрос: кликаем, убеждаемся, что нужный ответ соответствует вопросу')
    @pytest.mark.parametrize('question_id', [0, 1, 2, 3, 4, 5, 6, 7])
    