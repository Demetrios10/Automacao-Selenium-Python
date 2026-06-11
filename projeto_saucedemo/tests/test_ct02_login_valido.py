from projeto_saucedemo.pages.home_page import HomePage
from projeto_saucedemo.pages.login_page import LoginPage
import pytest

@pytest.mark.login
class TestCT02:
    def test_ct02_login_valido(self, driver):

        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        login_page.abrir_pagina()
        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.verificar_login_com_sucesso()
