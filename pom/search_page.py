from selenium.webdriver.common.by import By

from pom.base_page import BasePage


class SearchPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__searched_items_links_l = '.product-card-wrapper'
        self.__searched_items_titles_l = '.product-card__title'


    def find_item_in_serch_results_and_click(self, search_spec: str):
        list_of_res = self.are_present('css', self.__searched_items_links_l)

        for res in list_of_res:
            print(res.find_element(By.CSS_SELECTOR, self.__searched_items_titles_l).text)
            if search_spec in res.find_element(By.CSS_SELECTOR, self.__searched_items_titles_l).text:
                res.click()
                break


