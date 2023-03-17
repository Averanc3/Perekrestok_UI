import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )

@pytest.fixture(scope="function")
def setup(request):
    global driver
    browser_name = request.config.getoption("browser_name")
    if browser_name == "chrome":
        s = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=s)
    elif browser_name == "firefox":
        s = Service(GeckoDriverManager().install())
        driver = webdriver.Firefox(service=s)

    driver.get("https://www.perekrestok.ru/")
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.quit()




