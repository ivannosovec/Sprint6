import os
import sys
from base_page import *
from data import *
from locators.order_page_locators import *
from locators.main_page_locators import *

class OrderPage(BasePage):
    @allure.step("Заполнить информацию о клиенте")
    def fill_client_info(self, first_name, last_name, address, metro_station, phone):
        self.input_text(OrderPageLocators.INPUT_FIRST_NAME, first_name)
        self.input_text(OrderPageLocators.INPUT_LAST_NAME, last_name)
        self.input_text(OrderPageLocators.INPUT_ADDRESS, address)
        self.select_metro_station(metro_station)
        self.input_text(OrderPageLocators.INPUT_PHONE, phone)

    @allure.step("Выбрать станцию метро {metro_station}")
    def select_metro_station(self, metro_station):
        self.click_element(OrderPageLocators.INPUT_METRO_STATION)
        self.input_text(OrderPageLocators.INPUT_METRO_STATION, metro_station)
        self.click_element(OrderPageLocators.METRO_STATION_OPTION)

    @allure.step("Нажать кнопку 'Далее'")
    def click_next_button(self):
        self.click_element(OrderPageLocators.BUTTON_NEXT)

    @allure.step("Заполнить информацию об аренде")
    def fill_rental_info(self, date, rental_period, color, comment):
        self.select_rental_period(rental_period)
        self.set_delivery_date(date)
        self.select_color(color)
        self.add_comment(comment)

    @allure.step("Установить дату доставки {date}")
    def set_delivery_date(self, date):
        self.input_text(OrderPageLocators.INPUT_DATE, date)

    @allure.step("Выбрать срок аренды {rental_period}")
    def select_rental_period(self, rental_period):
        self.click_element(OrderPageLocators.INPUT_RENTAL_PERIOD)
        rental_period_locator = OrderPageLocators.get_rental_period_locator(rental_period)
        self.click_element(rental_period_locator)

    @allure.step("Выбрать цвет {color}")
    def select_color(self, color):
        if color == "black":
            self.click_element(OrderPageLocators.INPUT_COLOR_BLACK)
        elif color == "gray":
            self.click_element(OrderPageLocators.INPUT_COLOR_GRAY)

    @allure.step("Добавить комментарий {comment}")
    def add_comment(self, comment):
        self.input_text(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step("Нажать кнопку 'Заказать'")
    def click_order_button(self):
        self.click_element(OrderPageLocators.BUTTON_ORDER)

    @allure.step("Подтвердить заказ")
    def confirm_order(self):
        self.click_element(OrderPageLocators.BUTTON_CONFIRM_ORDER)

    @allure.step("Проверить успешное сообщение")
    def check_success_message(self):
        success_message = self.get_text(OrderPageLocators.SUCCESS_MESSAGE)
        return "Заказ оформлен" in success_message

    @allure.step("Выполнить флоу заказа")
    def execute_order_flow(self, order_data):
        self.fill_client_info(
            order_data["first_name"],
            order_data["last_name"],
            order_data["address"],
            order_data["metro_station"],
            order_data["phone"]
        )
        self.click_next_button()
        self.fill_rental_info(
            order_data["date"],
            order_data["rental_period"],
            order_data["color"],
            order_data["comment"]
        )
        self.click_order_button()
        self.confirm_order()
        return self.check_success_message()