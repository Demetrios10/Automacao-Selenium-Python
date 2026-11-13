"""Gerenciamento do navegador, independente dos Page Objects."""

from contextlib import contextmanager

from selenium import webdriver


@contextmanager
def sessao_chrome(headless=False, timeout=20):
    options = webdriver.ChromeOptions()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,900")
    browser = webdriver.Chrome(options=options)
    try:
        browser.set_page_load_timeout(timeout)
        yield browser
    finally:
        browser.quit()
