import pytest
from selenium import webdriver


@pytest.fixture(autouse=True)
def get_driver(request):
    driver = webdriver.Chrome()
    driver.get('https://saucedemo.com')
    driver.maximize_window()

    yield driver

    driver.quit()
