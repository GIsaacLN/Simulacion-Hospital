import asyncio
from concurrency import lanzar_concurrencia
from parallel import diagnostico_parallel
from async_tasks import diagnostico_asincrono
from utils import generar_pacientes
import time

def main():
    # Simulación concurrente
    print("=== Simulación de concurrencia ===")
    start = time.perf_counter()
    lanzar_concurrencia(num_pacientes=10, num_enfermeros=3)
    end = time.perf_counter()
    concurrent_time = end - start
    print(f"Tiempo concurrencia: {concurrent_time:.2f} segundos")

    # Simulación paralela
    print("\n=== Simulación de paralelismo ===")
    lotes = [list(range(10000)) for _ in range(4)]
    start = time.perf_counter()
    resultados = diagnostico_parallel(lotes)
    end = time.perf_counter()
    parallel_time = end - start
    print(f"Tiempo paralelismo: {parallel_time:.2f} segundos")

    # Simulación asíncrona
    print("\n=== Simulación asíncrona ===")
    pacientes = generar_pacientes(5)
    async def ejecutar_diagnostico_asincrono(pacientes):
        await asyncio.gather(*(diagnostico_asincrono(p) for p in pacientes))

    start = time.perf_counter()
    asyncio.run(ejecutar_diagnostico_asincrono(pacientes))
    end = time.perf_counter()
    async_time = end - start
    print(f"Tiempo asincronía: {async_time:.2f} segundos")

if __name__ == "__main__":
    main()
