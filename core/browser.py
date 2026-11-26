"""Gerenciamento do navegador, independente dos Page Objects."""

from collections.abc import Iterator
from contextlib import contextmanager

from selenium import webdriver

TAMANHO_JANELA = "1440,900"
TIMEOUT_PADRAO_SEGUNDOS = 20


@contextmanager
def sessao_chrome(
    headless: bool = False, timeout: int = TIMEOUT_PADRAO_SEGUNDOS
) -> Iterator[webdriver.Chrome]:
    browser = webdriver.Chrome(options=_opcoes_chrome(headless))
    try:
        browser.set_page_load_timeout(timeout)
        yield browser
    finally:
        browser.quit()


def _opcoes_chrome(headless: bool) -> webdriver.ChromeOptions:
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument(f"--window-size={TAMANHO_JANELA}")
    return options
