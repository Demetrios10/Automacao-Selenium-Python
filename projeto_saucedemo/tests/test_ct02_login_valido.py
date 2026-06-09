from projeto_saucedemo.pages.home_page import HomePage
from projeto_saucedemo.pages.login_page import LoginPage
import conftest
import pytest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login

class TestCT02:
    def test_ct02_login_valido(self):

        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page  = HomePage()

        # faz o login
        login_page.fazer_login("standard_user","secret_sauce")

        #verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()
