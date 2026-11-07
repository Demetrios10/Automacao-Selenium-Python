"""Demonstra preenchimento do cadastro sem enviar dados."""
import argparse
from core.browser import sessao_chrome
from pages.register_page import RegisterPage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--headless", action="store_true")
    args = parser.parse_args()
    with sessao_chrome(headless=args.headless) as browser:
        page = RegisterPage(browser).abrir()
        page.preencher(nome="Pessoa", sobrenome="Teste",
                       email="qa@example.com", telefone="1198765432")
        page.selecionar_genero("feminino").definir_hobby("filmes")
        if page.valor("nome") != "Pessoa" or not page.validade("email")["valid"]:
            raise AssertionError("Preenchimento não foi confirmado.")
        print("Preenchimento validado. Nenhum cadastro enviado.")


if __name__ == "__main__":
    main()
