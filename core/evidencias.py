"""Evidências por execução, sem dados reais de cadastro."""
from datetime import datetime, timezone
from pathlib import Path
import traceback


def criar_pasta(nome):
    raiz = Path(__file__).resolve().parents[1] / "evidencias" / "execucoes"
    instante = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%S%fZ")
    pasta = raiz / f"{instante}_{nome}"
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta


def registrar_erro(pasta):
    (pasta / "erro.txt").write_text(traceback.format_exc(), encoding="utf-8")


def capturar(browser, pasta):
    """Captura o estado final; problemas de captura não alteram o teste."""
    try:
        if not browser.save_screenshot(str(pasta / "tela-final.png")):
            raise RuntimeError("O navegador não gravou a captura.")
        (pasta / "pagina.txt").write_text(
            f"URL: {browser.current_url}\nTítulo: {browser.title}\n",
            encoding="utf-8")
    except Exception:
        registrar_erro(pasta)
