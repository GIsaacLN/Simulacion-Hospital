from src.concurrency import lanzar_concurrencia

def test_lanzar_concurrencia_simple():
    # No lanza excepción al procesar pocos pacientes
    lanzar_concurrencia(num_pacientes=3, num_enfermeros=1)
