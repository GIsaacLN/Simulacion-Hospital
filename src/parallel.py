from concurrent.futures import ProcessPoolExecutor
import os
import numpy as np

def analisis_intensivo(data):
    """
    Simula un análisis intensivo de datos.
    """
    arr = np.array(data)
    return np.sum(arr ** 2)

def diagnostico_parallel(lotes_datos):
    """
    Usa multiprocessing para procesar lotes de datos de diagnóstico.
    """
    with ProcessPoolExecutor(max_workers=os.cpu_count()) as executor:
        resultados = list(executor.map(analisis_intensivo, lotes_datos))
    return resultados
