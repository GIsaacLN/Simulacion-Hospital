import random
import time
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

def generar_pacientes(n):
    """
    Genera una lista de IDs de pacientes.
    """
    return [f"paciente_{i+1}" for i in range(n)]

def registro(paciente):
    logging.info(f"Registrando {paciente}")
    time.sleep(random.uniform(0.1, 0.3))

def seguimiento_y_alta(paciente):
    logging.info(f"Seguimiento y alta de {paciente}")
    time.sleep(random.uniform(0.1, 0.2))

def combinar_resultados(resultados):
    """
    Simula la combinación de resultados de APIs o modelos.
    """
    return sum(resultados) / len(resultados)
