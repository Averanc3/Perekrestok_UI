import time

import pytest

from pom.main_page import MainPage


@pytest.mark.usefixtures('setup')
class TestPerekrestok:

    def test_find_item_and_put_in_cart(self):
        main_page = MainPage(self.driver)
        main_page.fill_search_field_and_click('Lays')
        time.sleep(2)