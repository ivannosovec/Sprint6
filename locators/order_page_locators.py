from selenium.webdriver.common.by import By

class OrderPageLocators:
      INPUT_FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    INPUT_LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    INPUT_ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    INPUT_METRO_STATION = (By.XPATH, ".//input[@placeholder='* Станция метро']")
    INPUT_PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")
    BUTTON_NEXT = (By.XPATH, ".//button[text()='Далее']")
    METRO_STATION_OPTION = (By.CLASS_NAME, "select-search__row")
    INPUT_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    INPUT_RENTAL_PERIOD = (By.XPATH, ".//div[text()='* Срок аренды']")
    INPUT_COLOR_BLACK = (By.XPATH, ".//input[@id='black']")
    INPUT_COLOR_GRAY = (By.XPATH, ".//input[@id='grey']")
    INPUT_COMMENT = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")
    BUTTON_ORDER = (By.XPATH, ".//button[contains(@class, 'Button_Middle') and text()='Заказать']")
    BUTTON_CONFIRM_ORDER = (By.XPATH, ".//button[text()='Да']")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")

    @staticmethod
    def get_rental_period_locator(rental_period):
        return (By.XPATH, f".//div[contains(@class, 'Dropdown-option') and text()='{rental_period}']")