import requests

from pom.base_page import BasePage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search_field_l = '.search-form__inner input'
        self.__search_icon_l = '.search-form__search-icon'
        self.__footer_links_l = 'a.menu-link'

    def fill_search_field_and_click(self, textt):
        self.is_present('css', self.__search_field_l).send_keys(textt)
        self.is_present('css', self.__search_icon_l).click()

    def get_check_footer_links(self):
        footer_links = self.are_present('css', self.__footer_links_l)
        broken_links=[]
        for link in footer_links:
            url = link.get_attribute('href')

            result = requests.head(url)
            if result.status_code == 400:
                broken_links.append(url)

        print(broken_links)
        assert len(broken_links) == 0, f'Some broken link(s) there - {len(broken_links)}'


