"""Base unittest que registra o resultado de cada cenário."""

import json
import unittest
from datetime import UTC, datetime

from core.evidencias import criar_pasta


class EvidenceTestCase(unittest.TestCase):
    def run(self, result=None):
        self.pasta_evidencias = criar_pasta(self.id())
        inicio = datetime.now(UTC)
        result = result if result is not None else self.defaultTestResult()
        try:
            return super().run(result)
        finally:
            self._gravar_resultado(self._status(result), inicio)

    def _pertence(self, test) -> bool:
        """Subtestes e cenários ignorados chegam embrulhados em outro objeto."""
        return test is self or getattr(test, "test_case", None) is self

    def _tem_registro(self, entradas) -> bool:
        return any(self._pertence(test) for test, _ in entradas)

    def _status(self, result: unittest.TestResult) -> str:
        if self._tem_registro(result.errors):
            return "error"
        if self._tem_registro(result.failures):
            return "failed"
        if self._tem_registro(result.skipped):
            return "skipped"
        return "passed"

    def _gravar_resultado(self, status: str, inicio: datetime) -> None:
        dados = {
            "cenario": self.id(),
            "resultado": status,
            "inicio_utc": inicio.isoformat(),
            "fim_utc": datetime.now(UTC).isoformat(),
        }
        (self.pasta_evidencias / "resultado.json").write_text(
            json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
        )
