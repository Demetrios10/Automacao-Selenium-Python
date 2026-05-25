import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import conftest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        driver = conftest.driver
        driver.find_element(By.ID, "user-name").send_keys("standard_user")
        driver.find_element(By.ID, "password").send_keys("demo_sauce")
        driver.find_element(By.ID, "login-button").click()

        assert driver.find_element(By.XPATH, "//form/div[3]/h3").is_displayed()

        driver.save_screenshot("evidencias/login_invalido.png")
        driver.quit()
