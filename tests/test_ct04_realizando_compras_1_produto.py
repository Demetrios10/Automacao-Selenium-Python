from selenium.webdriver.common.by import By
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT04:
    def test_ct04_realizando_compras_1_produto(self):

        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_saucerr")


