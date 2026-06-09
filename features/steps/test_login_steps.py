"""
Steps para testes de Login
Usando Pytest + Selenium
"""
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
import os

# Adicionar o diretório raiz ao path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(__file__))))

from pages.login_page import LoginPage


class TestLoginSteps:
    """Testes de Login usando Page Object Model"""
    
    @pytest.fixture(autouse=True)
    def setup(self, driver):
        """Setup antes de cada teste"""
        self.driver = driver
        self.login_page = LoginPage(self.driver)
    
    def test_login_valido(self):
        """Teste de login com credenciais válidas"""
        # Dado que estou na página de login
        self.login_page.abrir_pagina()
        
        # Quando preencho o email e a senha
        self.login_page.preencher_email("usuario@teste.com")
        self.login_page.preencher_senha("senha123")
        
        # E clico no botão de login
        self.login_page.clicar_botao_login()
        
        # Então devo ser redirecionado para a página inicial
        assert self.driver.current_url.endswith("/home") or "home" in self.driver.current_url
    
    def test_login_invalido(self):
        """Teste de login com credenciais inválidas"""
        # Dado que estou na página de login
        self.login_page.abrir_pagina()
        
        # Quando preencho com credenciais inválidas
        self.login_page.preencher_email("usuario@teste.com")
        self.login_page.preencher_senha("senhaerrada")
        
        # E clico no botão de login
        self.login_page.clicar_botao_login()
        
        # Então devo ver mensagem de erro
        mensagem_erro = self.login_page.obter_mensagem_erro()
        assert "inválidas" in mensagem_erro.lower() or "erro" in mensagem_erro.lower()
