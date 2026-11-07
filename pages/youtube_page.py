"""Page Objects: elementos, ações e leitura de estado do YouTube."""
from urllib.parse import parse_qs, urlparse

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YouTubePage:
    URL = "https://www.youtube.com"
    CAMPO_PESQUISA = (By.CSS_SELECTOR, "input[name='search_query']")

    def __init__(self, browser, timeout=20):
        self.browser = browser
        self.timeout = timeout
        self.wait = WebDriverWait(browser, timeout)

    def abrir(self):
        self.browser.get(self.URL)
        return self

    def buscar(self, termo):
        campo = self.wait.until(EC.element_to_be_clickable(self.CAMPO_PESQUISA))
        campo.clear()
        campo.send_keys(termo, Keys.ENTER)
        return ResultadosPage(self.browser, self.timeout)


class ResultadosPage:
    TITULOS = (By.CSS_SELECTOR, "ytd-video-renderer a#video-title")

    def __init__(self, browser, timeout=20):
        self.browser = browser
        self.wait = WebDriverWait(browser, timeout)

    def termo_na_url(self):
        url = urlparse(self.browser.current_url)
        if url.path != "/results":
            return None
        termos = parse_qs(url.query).get("search_query", [])
        return termos[0] if len(termos) == 1 else None

    def aguardar_termo(self, termo):
        self.wait.until(
            lambda _: self.termo_na_url() == termo,
            "A URL não confirmou o termo pesquisado.")
        return self

    def titulos_visiveis(self):
        return [
            item.text.strip()
            for item in self.browser.find_elements(*self.TITULOS)
            if item.is_displayed() and item.text.strip()
        ]

    def aguardar_titulos(self):
        return self.wait.until(
            lambda _: self.titulos_visiveis(),
            "Nenhum vídeo visível foi encontrado.")
