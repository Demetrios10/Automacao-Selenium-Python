"""Fluxo de pesquisa e interface de linha de comando."""
import argparse

# Mantém compatibilidade com a execução direta do script.
if __package__ in (None, ""):
    import sys
    from pathlib import Path
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from core.browser import sessao_chrome
from pages.youtube_page import YouTubePage


def validar_entrada(termo, timeout):
    termo = termo.strip()
    if not termo:
        raise ValueError("Informe um termo de pesquisa.")
    if timeout <= 0:
        raise ValueError("O tempo limite deve ser positivo.")
    return termo


def pesquisar(browser, termo, timeout=20):
    """Orquestra as páginas; os seletores pertencem aos Page Objects."""
    termo = validar_entrada(termo, timeout)
    resultados = YouTubePage(browser, timeout).abrir().buscar(termo)
    resultados.aguardar_termo(termo)
    return resultados.aguardar_titulos()


def executar(termo="barcelona", headless=False, timeout=20):
    termo = validar_entrada(termo, timeout)
    with sessao_chrome(headless=headless, timeout=timeout) as browser:
        return pesquisar(browser, termo, timeout)


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
