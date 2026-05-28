import time

import pytest

from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self):
        mensagem_de_erro_esperada = (
            "Epic sadface: Username and password do not match any user in this service"
        )

        login_page = LoginPage()
        login_page.fazer_login("standard_user", "secret_saucerr")
        login_page.verificar_mensagem_de_erro_login_existe()
        login_page.verificar_texto_mensagem_de_erro_login(mensagem_de_erro_esperada)

