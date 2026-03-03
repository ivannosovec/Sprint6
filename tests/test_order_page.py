import os
import sys
from pages.base_page import *
from pages.order_page import *
import pytest
import allure
from data import *

class TestOrder:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()

        cls.home_page = HomePage(cls.driver)
        cls.order_page = OrderPage(cls.driver)

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

    def setup_method(self):
        self.home_page.open()

    @allure.title("Позитивный сценарий заказа")
    @pytest.mark.parametrize(
        "order_button_location, order_data",
        [
            ["top", TestData.ORDER_CLIENT_DATA_1],
            ["bottom", TestData.ORDER_CLIENT_DATA_2]
        ]
    )
    def test_order_positive_flow(self, order_button_location, order_data):
        if order_button_location == "top":
            self.home_page.click_order_button_top()
        else:
            self.home_page.click_order_button_bottom()

        assert self.order_page.execute_order_flow(order_data)

    @allure.title("Проверка перехода по логотипу Самоката")
    @allure.description("При клике на логотип Самоката пользователь должен попасть на главную страницу")
    def test_scooter_logo_redirect(self):
        self.home_page.click_scooter_logo()

        current_url = self.driver.current_url
        expected_url = self.home_page.base_url

        assert current_url == expected_url

    @allure.title("Проверка редиректа по логотипу Яндекса")
    @allure.description("При клике на логотип Яндекса пользователь должен попасть на главную страницу")
    def test_yandex_logo_redirect(self):
        self.home_page.click_yandex_logo()

        current_url = self.driver.current_url
        expected_url = self.home_page.base_url

        assert current_url == expected_url