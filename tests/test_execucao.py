"""Verifica o ciclo de vida sem abrir navegador nem acessar a internet."""
import unittest
from unittest.mock import Mock, patch

from scripts.pesquisa_youtube import executar


class TestExecucao(unittest.TestCase):
    @patch("scripts.pesquisa_youtube.webdriver.Chrome")
    @patch("scripts.pesquisa_youtube.pesquisar")
    def test_fecha_navegador_apos_sucesso(self, pesquisar, chrome):
        pesquisar.return_value = ["Vídeo de exemplo"]
        self.assertEqual(executar(), ["Vídeo de exemplo"])
        chrome.return_value.quit.assert_called_once()

    @patch("scripts.pesquisa_youtube.webdriver.Chrome")
    @patch("scripts.pesquisa_youtube.pesquisar")
    def test_fecha_navegador_apos_falha(self, pesquisar, chrome):
        pesquisar.side_effect = RuntimeError("Falha de busca")
        with self.assertRaisesRegex(RuntimeError, "Falha de busca"):
            executar()
        chrome.return_value.quit.assert_called_once()

    @patch("scripts.pesquisa_youtube.webdriver.Chrome")
    def test_fecha_navegador_se_configuracao_falhar(self, chrome):
        chrome.return_value.set_page_load_timeout.side_effect = RuntimeError("timeout")
        with self.assertRaises(RuntimeError):
            executar()
        chrome.return_value.quit.assert_called_once()

    @patch("scripts.pesquisa_youtube.webdriver.Chrome")
    def test_rejeita_entradas_invalidas_antes_de_abrir_chrome(self, chrome):
        for termo, timeout in [("   ", 20), ("python", 0), ("python", -1)]:
            with self.subTest(termo=termo, timeout=timeout):
                with self.assertRaises(ValueError):
                    executar(termo=termo, timeout=timeout)
        chrome.assert_not_called()


if __name__ == "__main__":
    unittest.main()
