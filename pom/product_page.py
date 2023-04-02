import time
import re

from pom.base_page import BasePage


class ProductPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__add_to_cart_button_l = '(//span[contains(text(), "корзину")])[2]'
        self.__add_more_to_cart_button_l = '(//div[@class = "cart-control__content"])[2]/button[2]'
        self.__delivery_status_submit = '.delivery-status__submit'
        self.__items_price_l = '.price-new'



    def add_to_cart(self, count):
        self.is_present('xpath', self.__add_to_cart_button_l).click()
        time.sleep(1)
        self.clear_fill_submit_address_text_field()
        time.sleep(1)
        if count > 1:
            for i in range(count):
                self.is_present('xpath', self.__add_more_to_cart_button_l).click()


    def get_added_items_count_price(self, count):
        counts_price_we_txt = self.is_present('css', self.__items_price_l).get_attribute("innerHTML")
        counts_price = re.findall("\d+,\d+", counts_price_we_txt)[0]
        print(counts_price)
        return count * float(counts_price.replace(',', '.'))


