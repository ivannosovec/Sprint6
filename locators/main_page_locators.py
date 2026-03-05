from selenium.webdriver.common.by import By

class MainPageLocators:
    # локатор кнопки яндекса
    YANDEX_BUTTON = (By.XPATH, '//a[@class = "Header_LogoYandex__3TSOI"]')
    # локатор лого 
    DZEN_LOGO = (By.XPATH, '//a[@data-testid = "logo"]')
    # локатор кнопки самокат
    SAMOKAT_BUTTON = (By.XPATH, '//a[@class = "Header_LogoScooter__3lsAR"]')
    # локатор картинки самокат на главной странице
    SAMOKAT_IMG = (By.XPATH, '//img[@alt = "Scooter blueprint"]')
    # локатор верхней кнопки Заказать
    ORDER_TOP_BUTTON = (By.XPATH, '//div[@class = "Header_Nav__AGCXC"]/button[text() = "Заказать"]')
    # локатор нижней кнопки Заказать
    ORDER_BOTTOM_BUTTON = (By.XPATH, '//div[@class = "Home_FinishButton__1_cWm"]/button[text() = "Заказать"]')

    # локаторы стрелочки вопроса
    QUEST_ARROW = [(By.XPATH, '//div[@id="accordion__heading-0"]'),
                   (By.XPATH, '//div[@id="accordion__heading-1"]'),
                   (By.XPATH, '//div[@id="accordion__heading-2"]'),
                   (By.XPATH, '//div[@id="accordion__heading-3"]'),
                   (By.XPATH, '//div[@id="accordion__heading-4"]'),
                   (By.XPATH, '//div[@id="accordion__heading-5"]'),
                   (By.XPATH, '//div[@id="accordion__heading-6"]'),
                   (By.XPATH, '//div[@id="accordion__heading-7"]')]
    # локаторы ответа 
    QUEST_ANSWER = [(By.XPATH, '//div[@id="accordion__panel-0"]'),
                   (By.XPATH, '//div[@id="accordion__panel-1"]'),
                   (By.XPATH, '//div[@id="accordion__panel-2"]'),
                   (By.XPATH, '//div[@id="accordion__panel-3"]'),
                   (By.XPATH, '//div[@id="accordion__panel-4"]'),
                   (By.XPATH, '//div[@id="accordion__panel-5"]'),
                   (By.XPATH, '//div[@id="accordion__panel-6"]'),
                   (By.XPATH, '//div[@id="accordion__panel-7"]')]