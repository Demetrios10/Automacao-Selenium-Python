import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

@pytest.mark.usefixtures("setup_teardown")
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = webdriver.Chrome()
        driver.implicitly_wait(5)
        driver.maximize_window()
        driver.get("https://www.saucedemo.com/")
        time.sleep(5)

        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("demo_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//form/div[3]/h3").is_displayed()

        driver.save_screenshot("evidencias/login_invalido.png")
        driver.quit()
