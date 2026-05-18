try:
    import pytest  # type: ignore[import]
except ImportError:
    pytest = None


@pytest.mark.simulacao if pytest else (lambda x: x)
class TestSimulacao():
  def test_simulacao_1(self):
    assert 1 == 1
    
  def test_simulacao_2(self):
    assert 'Demetrios' != 'Doglas'