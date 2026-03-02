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

class TestPageButtonsNavigation:
    @allure.title('Проверка навигации на главную страницу по кнопке самоката')
    @allure.description('Проверяем навигацию: переходим на заказ, кликаем на лого самоката, убеждаемся, что вернулись на главную страницу')
    def test_main_page_navigation_when_samokat_clicked(self, driver):
        nav_page=MainPageSamokat(driver)
        nav_page.click_top_order_button()
        nav_page.click_samokat_button()
        assert nav_page.check_main_page_address()

    @allure.title('Проверка навигации на страницу Дзен по кнопке Яндекса')
    @allure.description('Проверяем навигацию: переходим на заказ, кликаем на лого Яндекс, убеждаемся, что перешли на страницу Дзен')
    def test_dzen_page_navigation_when_yandex_clicked(self, driver):
        nav_page=MainPageSamokat(driver)
        nav_page.click_top_order_button()
        nav_page.click_yandex_button()
        assert nav_page.check_dzen_page_address()