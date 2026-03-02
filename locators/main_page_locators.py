from selenium.webdriver.common.by import By

class MainPageLocators:
    # локатор кнопки яндекса
    yandex_button = (By.XPATH, '//a[@class = "Header_LogoYandex__3TSOI"]')
    # локатор лого 
    dzen_logo = (By.XPATH, '//a[@data-testid = "logo"]')
    # локатор кнопки самокат
    samokat_button = (By.XPATH, '//a[@class = "Header_LogoScooter__3lsAR"]')
    # локатор картинки самокат на главной стрц.
    samokat_img = (By.XPATH, '//img[@alt = "Scooter blueprint"]')
    # локатор верхней кнопки Заказать
    order_top_button = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    # локатор нижней кнопки Заказать
    order_bottom_button = (By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')

    # локаторы стрелочки вопроса
    quest_arrow = [(By.XPATH, '//div[@id="accordion__heading-0"]'),
                   (By.XPATH, '//div[@id="accordion__heading-1"]'),
                   (By.XPATH, '//div[@id="accordion__heading-2"]'),
                   (By.XPATH, '//div[@id="accordion__heading-3"]'),
                   (By.XPATH, '//div[@id="accordion__heading-4"]'),
                   (By.XPATH, '//div[@id="accordion__heading-5"]'),
                   (By.XPATH, '//div[@id="accordion__heading-6"]'),
                   (By.XPATH, '//div[@id="accordion__heading-7"]')]
    # локаторы ответа 
    quest_answer = [(By.XPATH, '//div[@id="accordion__panel-0"]'),
                   (By.XPATH, '//div[@id="accordion__panel-1"]'),
                   (By.XPATH, '//div[@id="accordion__panel-2"]'),
                   (By.XPATH, '//div[@id="accordion__panel-3"]'),
                   (By.XPATH, '//div[@id="accordion__panel-4"]'),
                   (By.XPATH, '//div[@id="accordion__panel-5"]'),
                   (By.XPATH, '//div[@id="accordion__panel-6"]'),
                   (By.XPATH, '//div[@id="accordion__panel-7"]')]