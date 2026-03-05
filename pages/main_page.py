import os
import sys
from base_page import *
from data import *
from locators.main_page_locators import *

class MainPageSamokat(BasePageSamokat):

    @allure.step('Клик на кнопку Яндекс')
    def click_yandex_button(self):
        self.click_on_element(MainPageLocators.yandex_button)
        self.switch_to_new_tab()
        self.wait_loading_of_element(MainPageLocators.dzen_logo)

    @allure.step('Клик на кнопку Самокат')
    def click_samokat_button(self):
        self.click_on_element(MainPageLocators.samokat_button)
        self.wait_loading_of_element(MainPageLocators.samokat_img)

    @allure.step('Клик на верхнюю кнопку Заказать')
    def click_top_order_button(self):
        self.click_on_element(MainPageLocators.order_top_button)

    @allure.step('Клик на нижнюю кнопку Заказать')
    def click_bottom_order_button(self):
        self.click_on_element(MainPageLocators.order_bottom_button)

    @allure.step('Скролл до стрелочки вопроса {quest_id}')
    def scroll_to_quest_arrow(self, quest_id):
        self.scroll_to_element(MainPageLocators.quest_arrow[quest_id])
        self.wait_loading_of_element(MainPageLocators.quest_arrow[quest_id])

    @allure.step('Клик на стрелочку вопроса {quest_id}')
    def click_quest_arrow(self, quest_id):
        self.click_on_element(MainPageLocators.quest_arrow[quest_id])

    @allure.step('Проверка показа ответа на вопрос {quest_id}')
    def check_quest_answer_displayed(self, quest_id):
        self.wait_loading_of_element(MainPageLocators.quest_answer[quest_id])
        return self.check_displayed_element(MainPageLocators.quest_answer[quest_id])

    @allure.step('Проверка текста ответа на вопрос {quest_id}')
    def check_quest_answer_text(self, quest_id):
        self.wait_loading_of_element(MainPageLocators.quest_answer[quest_id])
        return self.get_text_from_element(MainPageLocators.quest_answer[quest_id]) == TestData.test_answers[quest_id]