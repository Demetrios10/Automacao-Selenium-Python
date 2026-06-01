import time
from pages.home_page import HomePage
import pytest
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.login
class TestCT05:
    def test_ct05_realizando_compras_2_produto(self):

        # instancia os objetos a serem usados no teste
        login_page = LoginPage()
        home_page  = HomePage()

        # faz o login
        login_page.fazer_login("standard_user","secret_sauce")

        # verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # adicionando a mochila ao carrinho
        home_page.adicionar_produto_ao_carrinho("add-to-cart")

        # clicando no botão voltar para a página de produtos
        home_page.clicar(self.botao_voltar_produtos)

        # adicionando o produto Sauce Labs Bike Light ao carrinho
        home_page.adicionar_produto_ao_carrinho("add-to-cart-sauce-labs-bike-light")






        # seleciona carrinho
        home_page.seleciona_carrinho()

        # seleciona para processar o checkout
        home_page.seleciona_checkout()

        # seleciona para preencher os dados de compra
        home_page.dados_compra()

        # clicar no botão continuar
        home_page.botao_continuar()
        time.sleep(3)

        # clicar no botão finalizar
        home_page.botao_finalizar()
        time.sleep(3)



