import os
import sys
directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(directory)
sys.path.append(directory + '\\pages')
from pages.base_page import *
from pages.order_page import *
import pytest
import allure
from data import *

class TestOrderPageOrdering:
    @allure.title('Проверка флоу позитивного сценария создания заказа')
    @allure.description('Проверяем обе кнопки Заказать, заполнение формы заказа, всплывающее окно с сообщением об успешном создании заказа.')
    @pytest.mark.parametrize('dataset_id', [0, 1])
    def test_order_creation(self, driver, dataset_id):
        order_page=OrderPageSamokat(driver)
        order_page.scroll_to_order_button(dataset_id)
        order_page.click_order_button(dataset_id)
        order_page.fill_first_form(dataset_id)
        order_page.fill_second_form(dataset_id)
        order_page.wait_acception_form()
        order_page.click_accept_order_form()
        order_page.wait_success_form()
        assert order_page.check_order_success()