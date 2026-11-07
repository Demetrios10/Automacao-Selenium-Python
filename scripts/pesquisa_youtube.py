"""Pesquisa no YouTube com esperas explícitas e validação do resultado."""
import argparse
from urllib.parse import parse_qs, urlparse

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def pesquisar(browser, termo, timeout=20):
    """Retorna os títulos visíveis; falha se a busca não produzir vídeos."""
    termo = termo.strip()
    if not termo:
        raise ValueError("Informe um termo de pesquisa.")
    if timeout <= 0:
        raise ValueError("O tempo limite deve ser positivo.")
    wait = WebDriverWait(browser, timeout)
    browser.get("https://www.youtube.com")
    campo = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "input[name='search_query']")))
    campo.clear()
    campo.send_keys(termo, Keys.ENTER)

    def busca_correta(driver):
        url = urlparse(driver.current_url)
        return (url.path == "/results"
                and parse_qs(url.query).get("search_query") == [termo])

    wait.until(busca_correta, "A URL não confirmou o termo pesquisado.")

    def titulos_visiveis(driver):
        return [
            item.text.strip()
            for item in driver.find_elements(
                By.CSS_SELECTOR, "ytd-video-renderer a#video-title")
            if item.is_displayed() and item.text.strip()
        ]

    return wait.until(titulos_visiveis, "Nenhum vídeo visível foi encontrado.")


def executar(termo="barcelona", headless=False, timeout=20):
    """Cria e encerra uma sessão independente, inclusive quando a busca falha."""
    if not termo.strip():
        raise ValueError("Informe um termo de pesquisa.")
    if timeout <= 0:
        raise ValueError("O tempo limite deve ser positivo.")
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    browser = webdriver.Chrome(options=options)
    try:
        browser.set_page_load_timeout(timeout)
        return pesquisar(browser, termo, timeout)
    finally:
        browser.quit()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--termo", default="barcelona")
    parser.add_argument("--headless", action="store_true")
    parser.add_argument("--timeout", type=float, default=20)
    args = parser.parse_args()
    titulos = executar(args.termo, args.headless, args.timeout)
    print(f"Busca validada: {len(titulos)} vídeos visíveis encontrados.")
    for titulo in titulos[:5]:
        print(f"- {titulo}")


if __name__ == "__main__":
    main()
