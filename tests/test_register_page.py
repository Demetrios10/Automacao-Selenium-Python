"""Testes unitários do contrato do Page Object, sem navegador real."""

from unittest.mock import Mock

from core.test_case import EvidenceTestCase
from pages.register_page import RegisterPage


class TestRegisterPage(EvidenceTestCase):
    def setUp(self):
        self.browser = Mock()
        self.page = RegisterPage(self.browser, timeout=0.01)

    def test_campo_desconhecido(self):
        with self.assertRaises(ValueError):
            self.page.campo("inexistente")

    def test_dados_invalidos_nao_preenchem_parcialmente(self):
        with self.assertRaises(ValueError):
            self.page.preencher(nome="Teste", inexistente="x")
        self.browser.find_element.assert_not_called()

    def test_genero_desconhecido(self):
        with self.assertRaises(ValueError):
            self.page.selecionar_genero("inexistente")

    def test_hobby_desconhecido(self):
        with self.assertRaises(ValueError):
            self.page.definir_hobby("inexistente")

    def test_marca_hobby_desmarcado(self):
        campo = self.browser.find_element.return_value
        campo.is_selected.return_value = False
        self.page.definir_hobby("filmes")
        campo.click.assert_called_once()

    def test_nao_desmarca_hobby_ja_marcado(self):
        campo = self.browser.find_element.return_value
        campo.is_selected.return_value = True
        self.page.definir_hobby("filmes")
        campo.click.assert_not_called()

    def test_desmarca_hobby_marcado(self):
        campo = self.browser.find_element.return_value
        campo.is_selected.return_value = True
        self.page.definir_hobby("filmes", False)
        campo.click.assert_called_once()

    def test_nao_clica_em_hobby_ja_desmarcado(self):
        campo = self.browser.find_element.return_value
        campo.is_selected.return_value = False
        self.page.definir_hobby("filmes", False)
        campo.click.assert_not_called()
