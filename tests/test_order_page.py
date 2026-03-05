import os
import sys
from pages.base_page import *
from pages.order_page import *
import pytest
import allure
from data import *

@allure.title('Проверка позитивного сценария оформления заказа')
    @allure.description('Тестирование функциональности оформления заказа с двумя наборами тестовых данных')
    @pytest.mark.parametrize('test_data', [TestData.test_data_user_1, TestData.test_data_user_2])
    def test_success_order(self, test_data, start_from_order_page):
        order_page = OrderPage(start_from_order_page)
        order_page.data_entry_first_form(test_data)
        order_page.data_entry_second_form(test_data)
        assert order_page.check_order_created_text_visibility()