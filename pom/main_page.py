from pom.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search_field_l = '.search-form__inner input'
        self.__search_icon_l = '.search-form__search-icon'

    def fill_search_field_and_click(self, textt):
        self.is_present('css', self.__search_field_l).send_keys(textt)
        self.is_present('css', self.__search_icon_l).click()
