from pages.home_page import HomePage
from pages.login_page import LoginPage
import pytest

@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login

class TestCT03:
    def test_ct03_login_invalido(self):

    # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page  = HomePage()

        # faz o login
        login_page.fazer_login("standard_user","secret_saucerr")

        # verifica que login não foi feito com sucesso e a mensagem de erro apareceu
        login_page.verificar_mensagem_de_erro_login()
