"""Valida evidências sem abrir navegador."""

import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from core.test_case import EvidenceTestCase


class TestEvidenceResult(EvidenceTestCase):
    def executar(self, case):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder)
            with patch("core.test_case.criar_pasta", return_value=path):
                case.run(unittest.TestResult())
            return json.loads((path / "resultado.json").read_text(encoding="utf-8"))

    def test_aprovado(self):
        class Case(EvidenceTestCase):
            def runTest(self):
                pass

        self.assertEqual(self.executar(Case())["resultado"], "passed")

    def test_reprovado(self):
        class Case(EvidenceTestCase):
            def runTest(self):
                self.fail("Falha deliberada da verificação do coletor")

        self.assertEqual(self.executar(Case())["resultado"], "failed")

    def test_erro_na_preparacao(self):
        class Case(EvidenceTestCase):
            def setUp(self):
                raise RuntimeError("Falha deliberada de preparação")

            def runTest(self):
                pass

        self.assertEqual(self.executar(Case())["resultado"], "error")

    def test_ignorado(self):
        @unittest.skip("Verificação do coletor")
        class Case(EvidenceTestCase):
            def runTest(self):
                pass

        self.assertEqual(self.executar(Case())["resultado"], "skipped")
