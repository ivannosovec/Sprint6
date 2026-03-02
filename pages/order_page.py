import os
import sys
directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(directory)
sys.path.append(directory + '\\locators')
from base_page import *
from data import *
from locators.order_page_locators import *
from locators.main_page_locators import *


class OrderPageSamokat(BasePageSamokat):
    @allure.step('Скролл до кнопки Заказать')
    def scroll_to_order_button(self, dataset):
        if dataset == 0:
            self.scroll_to_element(MainPageLocators.order_top_button)
        else:
            self.scroll_to_element(MainPageLocators.order_bottom_button)
            self.wait_loading_of_element(MainPageLocators.order_bottom_button)
    
    @allure.step('Клик на кнопку Заказать')
    def click_order_button(self, dataset):
        if dataset == 0:
            self.click_on_element(MainPageLocators.order_top_button)
        else:
            self.click_on_element(MainPageLocators.order_bottom_button)

    @allure.step('Заполнение первой формы заказа данными {dataset} и клик по кнопке Далее')
    def fill_first_form(self, dataset):
        self.set_element(OrderPageLocators.first_name_field, TestData.test_data_sets[dataset]['Имя'])
        self.set_element(OrderPageLocators.last_name_field, TestData.test_data_sets[dataset]['Фамилия'])
        self.set_element(OrderPageLocators.address_field, TestData.test_data_sets[dataset]['Адрес'])
        self.click_on_element(OrderPageLocators.metro_field)
        self.wait_loading_of_element(OrderPageLocators.metro_station[TestData.test_data_sets[dataset]['Метро']])
        self.click_on_element(OrderPageLocators.metro_station[TestData.test_data_sets[dataset]['Метро']])
        self.set_element(OrderPageLocators.phone_field, TestData.test_data_sets[dataset]['Телефон'])
        self.click_on_element(OrderPageLocators.next_button)

    @allure.step('Заполнение второй формы заказа данными {dataset} и клик по кнопке Заказать')
    def fill_second_form(self, dataset):
        self.click_on_element(OrderPageLocators.when_field)
        self.wait_loading_of_element(OrderPageLocators.day_when[TestData.test_data_sets[dataset]['Когда']])
        self.click_on_element(OrderPageLocators.day_when[TestData.test_data_sets[dataset]['Когда']])
        self.click_on_element(OrderPageLocators.term_field)
        self.wait_loading_of_element(OrderPageLocators.term_long[TestData.test_data_sets[dataset]['Срок']])
        self.click_on_element(OrderPageLocators.term_long[TestData.test_data_sets[dataset]['Срок']])
        self.click_on_element(OrderPageLocators.color_checkbox[TestData.test_data_sets[dataset]['Цвет']])
        self.set_element(OrderPageLocators.comment_field, TestData.test_data_sets[dataset]['Комментарий'])        
        self.click_on_element(OrderPageLocators.complete_order_button)

    @allure.step('Ожидание загрузки подтверждения отправки заказа')
    def wait_acception_form(self):
        self.wait_loading_of_element(OrderPageLocators.accept_order_button)

    @allure.step('Подтверждение отправки заказа')
    def click_accept_order_form(self):
        self.click_on_element(OrderPageLocators.accept_order_button)

    @allure.step('Ожидание загрузки сообщения об успешном заказе')
    def wait_success_form(self):
        self.wait_loading_of_element(OrderPageLocators.check_status_button)

    @allure.step('Проверка успешного создания заказа')
    def check_order_success(self):
        return TestData.success_title in self.get_text_from_element(OrderPageLocators.success_message)