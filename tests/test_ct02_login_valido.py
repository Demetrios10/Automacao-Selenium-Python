from selenium.webdriver.common.by import By
from pages.login_page import LoginPage
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login

class TestCT02:
    def test_ct02_login_valido(self):
        driver = conftest.driver
        login_page = LoginPage()
        
        login_page.fazer_login("standart_user" , "secret_sauce")
        
        assert driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span").is_displayed()
        
        # salva a evidência
        driver.save_screenshot("evidencias/login_valido.png")
