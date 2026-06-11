from selenium.webdriver.common.by import By
from projeto_saucedemo.pages.base_page import BasePage


class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username_field = (By.ID, "user-name")
        self.password_field = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.erro_message_login = (By.XPATH, "//h3[@data-test='error']")

    def abrir_pagina(self):
        self.driver.get("https://www.saucedemo.com/")

    def preencher_email(self, usuario):
        self.escrever(self.username_field, usuario)

    def preencher_senha(self, senha):
        self.escrever(self.password_field, senha)

    def clicar_botao_login(self):
        self.clicar(self.login_button)

    def obter_mensagem_erro(self):
        return self.pegar_texto_elemento(self.erro_message_login)

    def fazer_login(self, usuario, senha):
        self.preencher_email(usuario)
        self.preencher_senha(senha)
        self.clicar_botao_login()

    def verificar_mensagem_de_erro_login_existe(self):
        self.verificar_se_elemento_existe(self.erro_message_login)

    def verificar_texto_mensagem_de_erro_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.erro_message_login).strip()
        assert (
            texto_encontrado == texto_esperado
        ), f"O texto retornado foi '{texto_encontrado}', mas era esperado '{texto_esperado}'."
