"""Cenários reais: habilite RUN_E2E=1. Uma sessão isolada por teste."""
import os
import unittest
from core.browser import sessao_chrome
from pages.register_page import RegisterPage
from core.evidencias import criar_pasta, registrar_erro, capturar


@unittest.skipUnless(os.getenv("RUN_E2E") == "1", "Requer RUN_E2E=1 e Chrome")
class TestRegisterE2E(unittest.TestCase):
    def setUp(self):
        self.pasta_evidencias = criar_pasta(self._testMethodName)
        self.session = sessao_chrome(headless=os.getenv("HEADLESS") == "1")
        try:
            self.browser = self.session.__enter__()
        except Exception:
            registrar_erro(self.pasta_evidencias)
            raise
        self.addCleanup(self.session.__exit__, None, None, None)
        self.addCleanup(capturar, self.browser, self.pasta_evidencias)
        self.page = RegisterPage(self.browser).abrir()

    def test_nome_e_sobrenome(self):
        self.page.preencher(nome="Pessoa", sobrenome="Teste")
        self.assertEqual(self.page.valor("nome"), "Pessoa")
        self.assertEqual(self.page.valor("sobrenome"), "Teste")

    def test_nome_obrigatorio(self):
        self.assertTrue(self.page.validade("nome")["valueMissing"])

    def test_email_invalido(self):
        self.page.preencher(email="email-invalido")
        self.assertTrue(self.page.validade("email")["typeMismatch"])

    def test_email_valido(self):
        self.page.preencher(email="qa@example.com")
        self.assertTrue(self.page.validade("email")["valid"])

    def test_telefone_nove_digitos(self):
        self.page.preencher(telefone="123456789")
        self.assertTrue(self.page.validade("telefone")["patternMismatch"])

    def test_telefone_dez_digitos(self):
        self.page.preencher(telefone="1198765432")
        self.assertTrue(self.page.validade("telefone")["valid"])

    def test_generos_mutuamente_exclusivos(self):
        self.page.selecionar_genero("masculino").selecionar_genero("feminino")
        self.assertTrue(self.page.genero("feminino").is_selected())
        self.assertFalse(self.page.genero("masculino").is_selected())

    def test_multiplos_hobbies(self):
        self.page.definir_hobby("filmes").definir_hobby("hockey")
        self.assertTrue(self.page.hobby("filmes").is_selected())
        self.assertTrue(self.page.hobby("hockey").is_selected())

    def test_senhas_diferentes(self):
        self.page.preencher(senha="Teste123", confirmacao="Outra123")
        self.assertTrue(self.page.validade("confirmacao")["customError"])

    def test_senhas_iguais(self):
        self.page.preencher(senha="Teste123", confirmacao="Teste123")
        self.assertFalse(self.page.validade("confirmacao")["customError"])

    def test_refresh_limpa_nome(self):
        self.page.preencher(nome="Pessoa").atualizar()
        self.assertEqual(self.page.valor("nome"), "")
