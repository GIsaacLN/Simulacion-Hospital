import pytest
from src.async_tasks import diagnostico_asincrono

@pytest.mark.asyncio
async def test_diagnostico_asincrono_simple():
    resultado = await diagnostico_asincrono("test_paciente")
    assert isinstance(resultado, float)
