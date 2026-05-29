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

        # adicionando segundo produto ao carrinho
        home_page.adicionar_produto_ao_carrinho("Sauce Labs Backpack")

        # clicando no botão para finalizar a compra
        home_page.clicar_no_botao_finalizar_compra()
        time.sleep(5)






# preenchendo os campos para finalizar a compra
driver.find_element(By.ID,"first-name").send_keys("Douglas")
driver.find_element(By.ID,"last-name").send_keys("Gomes")
driver.find_element(By.ID,"postal-code").send_keys("04653432")
time.sleep(5)

# clicando no botão Continue
driver.find_element(By.ID,"continue").click()

# clicando no botão Finish
driver.find_element(By.ID,"finish").click()
time.sleep(5)

# verificando se o texto esta na tela
assert driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/span").is_displayed()

# salva a evidência
driver.save_screenshot("evidencias/compra_de_2_produtos.png")

driver.quit()
