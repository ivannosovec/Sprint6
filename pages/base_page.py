import os
import sys
directory = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
sys.path.append(directory)
from data import *
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class BasePageSamokat:

    # конструктор класса
    def __init__(self, driver):
        self.driver = driver
        driver.get(TestData.main_page_url)

    @allure.step('ждем прогрузку элемента')
    def wait_loading_of_element(self, locator):
        return WebDriverWait(self.driver, 30).until(expected_conditions.visibility_of_element_located(locator))
        
    @allure.step('переключаемся на новую вкладку')
    def switch_to_new_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('скролл до элемента')
    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script('arguments[0].scrollIntoView();', element)

    @allure.step('клик по элементу')
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('заполнить элемент')
    def set_element(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('вернуть текст элемента')
    def get_text_from_element(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('вернуть видимость элемента')
    def check_displayed_element(self, locator):
        return self.driver.find_element(*locator).is_displayed
    
    
    @allure.step('проверить адрес страницы Дзен')
    def check_dzen_page_address(self):
        return TestData.dzen_url in self.driver.current_url

    @allure.step('проверить адрес главной страницы')
    def check_main_page_address(self):
        return TestData.main_page_url == self.driver.current_url