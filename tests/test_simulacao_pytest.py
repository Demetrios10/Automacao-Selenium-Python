import pytest


@pytest.mark.simulacao
class TestSimulacao():
  def test_simulacao_1(self):
    assert 1 == 1
    
  def test_simulacao_2(self):
    assert 'Demetrios' != 'Doglas'