import asyncio
import random
import logging

async def llamar_api_modelo(paciente):
    latencia = random.uniform(0.1, 0.5)
    await asyncio.sleep(latencia)
    resultado = random.uniform(0.0, 1.0)
    logging.info(f"API modelo para {paciente} devolvió {resultado:.2f}")
    return resultado

async def diagnostico_asincrono(paciente):
    """
    Simula llamadas asíncronas a un modelo IA para diagnóstico.
    """
    tareas = [llamar_api_modelo(paciente) for _ in range(3)]
    resultados = await asyncio.gather(*tareas)
    from utils import combinar_resultados
    valor = combinar_resultados(resultados)
    logging.info(f"Diagnóstico asíncrono de {paciente}: {valor:.2f}")
    return valor
