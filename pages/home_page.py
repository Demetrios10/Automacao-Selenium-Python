from pages.base_page import BasePage
import conftest
from selenium.webdriver.common.by import By


class HomePage(BasePage):

    def __init__(self):
        self.driver = conftest.driver
        self.titulo_pagina = (By.XPATH,"//span[contains(@class,'title') and @data-test='title' and normalize-space()='Products']")

    def verificar_login_com_sucesso(self):
        self.verificar_se_elemento_existe(self.titulo_pagina)