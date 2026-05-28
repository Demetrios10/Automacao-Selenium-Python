from selenium.webdriver.common.by import By
from pages.home_page import HomePage
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT04:
    def test_ct04_realizando_compras_1_produto(self):

        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page  = HomePage()

        # faz o login
        login_page.fazer_login("standard_user","secret_sauce")

        #verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()


