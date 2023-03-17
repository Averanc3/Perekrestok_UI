import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BasePage():
    def __init__(self, driver):
        self.driver = driver
        self.__wait = WebDriverWait(driver, 15)

    def open(self):
        self.driver.get(self.url)

    def __get_selenium_by(self, find_by: str) -> dict:
        find_by = find_by.lower()
        locator = {
            'css' : By.CSS_SELECTOR,
            'xpath': By.XPATH,
            'class_name': By.CLASS_NAME,
            'id': By.ID,
            'link_text': By.LINK_TEXT,
            'name': By.NAME,
            'partial_link_text': By.PARTIAL_LINK_TEXT,
            'tag_name': By.TAG_NAME
        }
        return locator[find_by]

    def is_visible(self, find_by : str, locator: str):
        return self.__wait.until(EC.visibility_of_element_located((self.__get_selenium_by(find_by), locator)))

    def is_present(self, find_by: str, locator: str):
        return self.__wait.until(EC.presence_of_element_located((self.__get_selenium_by(find_by), locator)))

    def are_present(self, find_by: str, locator: str):
        return self.__wait.until(EC.presence_of_all_elements_located((self.__get_selenium_by(find_by), locator)))
