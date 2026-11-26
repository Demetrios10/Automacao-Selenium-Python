"""Evidências por execução, sem dados reais de cadastro."""

import traceback
from datetime import UTC, datetime
from pathlib import Path

RAIZ_EVIDENCIAS = Path(__file__).resolve().parents[1] / "evidencias" / "execucoes"


def criar_pasta(nome: str) -> Path:
    instante = datetime.now(UTC).strftime("%Y%m%dT%H%M%S%fZ")
    pasta = RAIZ_EVIDENCIAS / f"{instante}_{nome}"
    pasta.mkdir(parents=True, exist_ok=True)
    return pasta


def registrar_erro(pasta: Path) -> None:
    (pasta / "erro.txt").write_text(traceback.format_exc(), encoding="utf-8")


def capturar(browser, pasta: Path) -> None:
    """Captura o estado final; problemas de captura não alteram o teste."""
    try:
        if not browser.save_screenshot(str(pasta / "tela-final.png")):
            raise RuntimeError("O navegador não gravou a captura.")
        (pasta / "pagina.txt").write_text(
            f"URL: {browser.current_url}\nTítulo: {browser.title}\n", encoding="utf-8"
        )
    except Exception:
        registrar_erro(pasta)
