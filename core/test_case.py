"""Base unittest que registra o resultado de cada cenário."""

import json
import unittest
from datetime import datetime, timezone

from core.evidencias import criar_pasta


class EvidenceTestCase(unittest.TestCase):
    def run(self, result=None):
        self.pasta_evidencias = criar_pasta(self.id())
        started = datetime.now(timezone.utc)
        result = result if result is not None else self.defaultTestResult()
        try:
            return super().run(result)
        finally:

            def pertence(test):
                return test is self or getattr(test, "test_case", None) is self

            errors = [entry for entry in result.errors if pertence(entry[0])]
            failures = [entry for entry in result.failures if pertence(entry[0])]
            skipped = [entry for entry in result.skipped if pertence(entry[0])]
            status = (
                "error"
                if errors
                else "failed" if failures else "skipped" if skipped else "passed"
            )
            data = {
                "cenario": self.id(),
                "resultado": status,
                "inicio_utc": started.isoformat(),
                "fim_utc": datetime.now(timezone.utc).isoformat(),
            }
            (self.pasta_evidencias / "resultado.json").write_text(
                json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
            )
