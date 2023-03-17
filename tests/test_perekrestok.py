import time

import pytest

from pom.main_page import MainPage
from pom.search_page import SearchPage


@pytest.mark.usefixtures('setup')
class TestPerekrestok:

    def test_find_item_and_put_in_cart(self):
        main_page = MainPage(self.driver)
        main_page.fill_search_field_and_click('Lays')
        search_page = SearchPage(self.driver)
        search_page.find_item_in_serch_results_and_click('Stax')
        time.sleep(2)