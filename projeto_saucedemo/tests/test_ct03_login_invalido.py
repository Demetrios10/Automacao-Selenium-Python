import pytest

from projeto_saucedemo.pages.login_page import LoginPage


@pytest.mark.login
class TestCT03:
    def test_ct03_login_invalido(self, driver):
        mensagem_de_erro_esperada = (
            "Epic sadface: Username and password do not match any user in this service"
        )

        login_page = LoginPage(driver)
        login_page.abrir_pagina()
        login_page.fazer_login("standard_user", "secret_saucerr")
        login_page.verificar_mensagem_de_erro_login_existe()
        login_page.verificar_texto_mensagem_de_erro_login(mensagem_de_erro_esperada)

