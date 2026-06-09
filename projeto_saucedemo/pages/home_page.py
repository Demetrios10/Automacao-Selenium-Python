import time

from projeto_saucedemo.pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH,"//span[contains(@class,'title') and @data-test='title' and normalize-space()='Products']")
        self.item_inventario = (By.XPATH,"//div[@data-test='inventory-item-name' and normalize-space(.)='Sauce Labs Backpack']")
        self.adiciona_produto_ao_carrinho = (By.ID,"add-to-cart")
        self.carrinho = (By.XPATH,"//a[@data-test='shopping-cart-link']")
        self.botao_voltar_produtos = (By.ID,"continue-shopping")
        self.adiciona_produto2_ao_carrinho = (By.ID,"add-to-cart-sauce-labs-bike-light")
        self.carrinho = (By.XPATH,"//a[@data-test='shopping-cart-link']")
        self.checkout = (By.ID,"checkout")
        self.dados = (By.ID,"first-name"), (By.ID,"last-name"), (By.ID,"postal-code")
        self.continuar = (By.ID,"continue")
        self.finalizar = (By.ID,"finish")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def verificar_login_sem_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)

    def adicionar_produto_ao_carrinho(self, nome_item):
        item =self.item_inventario[0], self.item_inventario[1].format(nome_item)
        self.clicar(item)
        self.clicar(self.adiciona_produto_ao_carrinho)

    def seleciona_carrinho(self):
        self.clicar(self.carrinho)

    def seleciona_checkout(self):
        self.clicar((By.ID,"checkout"))

    def dados_compra(self):
        self.escrever(self.dados[0],"Deltas")
        self.escrever(self.dados[1],"Santos")
        self.escrever(self.dados[2],"0000")

    def botao_continuar(self):
        self.clicar(self.continuar)

    def botao_finalizar(self):
        self.clicar((By.ID,"finish"))


