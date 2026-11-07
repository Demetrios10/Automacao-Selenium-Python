"""Cenários de busca com DOM simulado e esperas reais do Selenium."""
import unittest
from unittest.mock import Mock, patch
from urllib.parse import quote_plus

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

from scripts.pesquisa_youtube import pesquisar, executar


class TestPesquisa(unittest.TestCase):
    def setUp(self):
        self.browser = Mock()
        self.browser.current_url = "https://www.youtube.com/results?search_query=barcelona"
        self.campo = self.browser.find_element.return_value
        self.campo.is_displayed.return_value = True
        self.campo.is_enabled.return_value = True
        self.browser.find_elements.return_value = [self.video(" Barcelona ")]
        self.wait_patch = patch(
            "scripts.pesquisa_youtube.WebDriverWait",
            side_effect=lambda browser, timeout: WebDriverWait(
                browser, timeout, poll_frequency=0.001))
        self.wait_patch.start()
        self.addCleanup(self.wait_patch.stop)

    @staticmethod
    def video(texto, visivel=True):
        video = Mock()
        video.text = texto
        video.is_displayed.return_value = visivel
        return video

    def test_busca_valida_e_envia_enter(self):
        self.assertEqual(pesquisar(self.browser, "barcelona", .02), ["Barcelona"])
        self.campo.clear.assert_called_once()
        self.campo.send_keys.assert_called_once_with("barcelona", Keys.ENTER)

    def test_remove_espacos_do_termo(self):
        pesquisar(self.browser, "  barcelona  ", .02)
        self.campo.send_keys.assert_called_once_with("barcelona", Keys.ENTER)

    def test_termo_com_acentos_espacos_e_simbolos(self):
        termo = "automação QA & Python"
        self.browser.current_url = (
            "https://www.youtube.com/results?search_query=" + quote_plus(termo))
        self.assertEqual(pesquisar(self.browser, termo, .02), ["Barcelona"])
        self.campo.send_keys.assert_called_once_with(termo, Keys.ENTER)

    def test_rejeita_termo_vazio_sem_navegar(self):
        for termo in ["", " ", "\t\n"]:
            with self.subTest(termo=termo), self.assertRaises(ValueError):
                pesquisar(self.browser, termo, .02)
        self.browser.get.assert_not_called()

    def test_rejeita_timeout_invalido_sem_navegar(self):
        for timeout in [0, -1]:
            with self.subTest(timeout=timeout), self.assertRaises(ValueError):
                pesquisar(self.browser, "barcelona", timeout)
        self.browser.get.assert_not_called()

    def test_falha_quando_url_tem_outro_termo(self):
        self.browser.current_url = "https://www.youtube.com/results?search_query=outro"
        with self.assertRaisesRegex(TimeoutException, "URL"):
            pesquisar(self.browser, "barcelona", .01)

    def test_falha_quando_nao_esta_na_pagina_de_resultados(self):
        self.browser.current_url = "https://www.youtube.com/?search_query=barcelona"
        with self.assertRaises(TimeoutException):
            pesquisar(self.browser, "barcelona", .01)

    def test_falha_quando_campo_nao_esta_habilitado(self):
        self.campo.is_enabled.return_value = False
        with self.assertRaises(TimeoutException):
            pesquisar(self.browser, "barcelona", .01)
        self.campo.send_keys.assert_not_called()

    def test_falha_quando_nao_ha_videos(self):
        self.browser.find_elements.return_value = []
        with self.assertRaisesRegex(TimeoutException, "Nenhum vídeo"):
            pesquisar(self.browser, "barcelona", .01)

    def test_ignora_titulos_vazios_e_videos_ocultos(self):
        self.browser.find_elements.return_value = [
            self.video(""), self.video("   "), self.video("Oculto", False),
            self.video(" Primeiro "), self.video("Segundo")]
        self.assertEqual(pesquisar(self.browser, "barcelona", .02),
                         ["Primeiro", "Segundo"])

    def test_aguarda_videos_carregados_depois(self):
        self.browser.find_elements.side_effect = [
            [], [], [self.video("Carregado depois")]]
        self.assertEqual(pesquisar(self.browser, "barcelona", .05),
                         ["Carregado depois"])

    def test_propaga_falha_de_navegacao(self):
        self.browser.get.side_effect = TimeoutException("Página indisponível")
        with self.assertRaisesRegex(TimeoutException, "Página indisponível"):
            pesquisar(self.browser, "barcelona", .01)


class TestConfiguracao(unittest.TestCase):
    @patch("scripts.pesquisa_youtube.webdriver.Chrome")
    @patch("scripts.pesquisa_youtube.pesquisar", return_value=["Vídeo"])
    def test_headless_e_timeout_personalizados(self, pesquisar_mock, chrome):
        executar("Python", headless=True, timeout=30)
        options = chrome.call_args.kwargs["options"]
        self.assertIn("--headless=new", options.arguments)
        chrome.return_value.set_page_load_timeout.assert_called_once_with(30)
        pesquisar_mock.assert_called_once_with(chrome.return_value, "Python", 30)

    @patch("scripts.pesquisa_youtube.webdriver.Chrome")
    @patch("scripts.pesquisa_youtube.pesquisar", return_value=["Vídeo"])
    def test_padrao_abre_janela(self, pesquisar_mock, chrome):
        executar()
        self.assertNotIn("--headless=new", chrome.call_args.kwargs["options"].arguments)


if __name__ == "__main__":
    unittest.main()
