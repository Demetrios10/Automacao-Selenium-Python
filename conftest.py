import pytest
from selenium import webdriver


driver: webdriver.remote


@pytest.fixture
def setup_teardown():
    global driver
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/")
    
    # run tests
    yield
    
    # teardown
    driver.quit()