from selenium.webdriver.common.by import By

class OrderPageLocators:
    # локатор поля Имя
    first_name_field = (By.XPATH, '//input[contains(@placeholder, "Имя")]')
    # локатор поля Фамилия
    last_name_field = (By.XPATH, '//input[contains(@placeholder, "Фамилия")]')
    # локатор  Адрес
    address_field = (By.XPATH, '//input[contains(@placeholder, "Адрес")]')
    # локатор  Станция метро
    metro_field = (By.XPATH, '//input[contains(@placeholder, "Станция")]')
    # локатор станций метро в выпадающем списке
    metro_station = [(By.XPATH, '//div[text()="Сокольники"]/parent::button'), 
                     (By.XPATH, '//div[text()="Черкизовская"]/parent::button')]
    # локатор поля Телефон
    phone_field = (By.XPATH, '//input[contains(@placeholder, "Телефон")]')
    # локатор кнопки Далее 
    next_button = (By.XPATH, '//button[contains(text(), "Далее")]')

    # локатор поля Когда привезти
    when_field = (By.XPATH, '//input[contains(@placeholder, "Когда")]')
    # локаторы дат Когда привезти
    day_when = [(By.XPATH, '//div[text()="27"]'),
                (By.XPATH, '//div[text()="28"]')]
    # локатор поля Срок аренды
    term_field = (By.XPATH, '//div[@class = "Dropdown-control"]')
    # локаторы вариантов Срока аренды
    term_long = [(By.XPATH, '//div[text()="двое суток"]'),
                (By.XPATH, '//div[text()="четверо суток"]')]
    # локаторы вариантов цвета
    color_checkbox = [(By.XPATH, '//input[@id="black"]'),
                (By.XPATH, '//input[@id="grey"]')]
    # локатор поля Комментарий
    comment_field = (By.XPATH, '//input[contains(@placeholder, "Комментарий")]')        
    # локатор кнопки Заказать 
    complete_order_button = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text() = "Заказать"]')

    # локатор модального окна подтверждения 
    accept_modal_window = (By.XPATH, '//div[@class="Order_Modal__YZ-d3"]')
    # локатор кнопки Да 
    accept_order_button = (By.XPATH, '//button[text()= "Да"]')

    # локатор сообщения об успешном создании заказа 
    success_message = (By.XPATH, '//div[@class="Order_ModalHeader__3FDaJ"]')
    # локатор кнопки Посмотреть статус в окне об успешном создании заказа 
    check_status_button = (By.XPATH, '//button[contains(text(), "Посмотреть")]')