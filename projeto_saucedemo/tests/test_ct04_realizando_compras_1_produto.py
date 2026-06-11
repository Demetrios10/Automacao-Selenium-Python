import pytest
from projeto_saucedemo.pages.home_page import HomePage
from projeto_saucedemo.pages.login_page import LoginPage


@pytest.mark.login
class TestCT04:
    def test_ct04_realizando_compras_1_produto(self, driver):

        login_page = LoginPage(driver)
        home_page = HomePage(driver)

        login_page.abrir_pagina()
        login_page.fazer_login("standard_user", "secret_sauce")

        home_page.verificar_login_com_sucesso()

        home_page.adicionar_produto_ao_carrinho("Sauce Labs Backpack")
        home_page.seleciona_carrinho()
        home_page.seleciona_checkout()
        home_page.dados_compra()
        home_page.botao_continuar()
        home_page.botao_finalizar()



