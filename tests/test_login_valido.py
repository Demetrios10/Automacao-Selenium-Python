from selenium.webdriver.common.by import By
import time
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
class TestCT02:
    def test_login_valido(self):
        driver = conftest.driver
        driver.find_element(By.ID,"user-name").send_keys("standard_user")
        driver.find_element(By.ID,"password").send_keys("secret_sauce")
        driver.find_element(By.ID,"login-button").click()
        time.sleep(10)
        
        assert driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span").is_displayed()
        
        # salva a evidência
        driver.save_screenshot("evidencias/login_valido.png")
