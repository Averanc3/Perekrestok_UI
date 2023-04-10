import time

import pytest

from pom.main_page import MainPage
from pom.product_page import ProductPage
from pom.search_page import SearchPage


@pytest.mark.usefixtures('setup')
class TestPerekrestok:

    def test_find_item_and_put_in_cart(self):
        count = 5
        main_page = MainPage(self.driver)
        main_page.fill_search_field_and_click('Lays')
        search_page = SearchPage(self.driver)
        search_page.find_item_in_serch_results_and_click('Stax')
        product_page = ProductPage(self.driver)
        product_page.add_to_cart(count)
        count_price = product_page.get_added_items_count_price(count)
        # cart_page = CartPage(self.driver)
        time.sleep(2)

    def test_footer_links_not_empty(self):
        main_page = MainPage(self.driver)
        # Need a better name
        main_page.find_and_get_footer_links()
