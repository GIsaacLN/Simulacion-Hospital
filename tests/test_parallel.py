import numbers
from src.parallel import diagnostico_parallel

def test_diagnostico_parallel_simple():
    lotes = [[1, 2, 3], [4, 5, 6]]
    resultados = diagnostico_parallel(lotes)
    # Verificamos que sea lista de números (int, float o np.generic)
    assert isinstance(resultados, list)
    assert all(isinstance(r, numbers.Number) for r in resultados)
