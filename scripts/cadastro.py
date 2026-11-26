"""Demonstra preenchimento do cadastro sem enviar dados."""

import argparse

from core.browser import sessao_chrome
from pages.register_page import RegisterPage

DADOS_DEMONSTRACAO = {
    "nome": "Pessoa",
    "sobrenome": "Teste",
    "email": "qa@example.com",
    "telefone": "1198765432",
}


def _argumentos() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--headless", action="store_true")
    return parser.parse_args()


def _preenchimento_confirmado(page: RegisterPage) -> bool:
    return page.valor("nome") == DADOS_DEMONSTRACAO["nome"] and page.validade("email")["valid"]


def main() -> None:
    args = _argumentos()
    with sessao_chrome(headless=args.headless) as browser:
        page = RegisterPage(browser).abrir()
        page.preencher(**DADOS_DEMONSTRACAO)
        page.selecionar_genero("feminino").definir_hobby("filmes")
        if not _preenchimento_confirmado(page):
            raise AssertionError("Preenchimento não foi confirmado.")
        print("Preenchimento validado. Nenhum cadastro enviado.")


if __name__ == "__main__":
    main()
