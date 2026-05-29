import time

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

        # verifica se o login foi realizado
        home_page.verificar_login_com_sucesso()

        # adicionando a mochila ao carrinho
        home_page.adicionar_produto_ao_carrinho("Sauce Labs Backpack")

        # clicar no botão para retornar para a página de produtos
        home_page.clicar_no_botao_voltar_para_produtos()
        time.sleep(15)


