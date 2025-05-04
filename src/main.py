import asyncio
from concurrency import lanzar_concurrencia
from parallel import diagnostico_parallel
from async_tasks import diagnostico_asincrono
from utils import generar_pacientes

def main():
    # Simulación concurrente
    print("=== Simulación de concurrencia ===")
    lanzar_concurrencia(num_pacientes=10, num_enfermeros=3)

    # Simulación paralela
    print("\n=== Simulación de paralelismo ===")
    lotes = [list(range(10000)) for _ in range(4)]
    resultados = diagnostico_parallel(lotes)
    print(f"Resultados paralelos: {resultados}")

    # Simulación asíncrona
    print("\n=== Simulación asíncrona ===")
    pacientes = generar_pacientes(5)
    async def ejecutar_diagnostico_asincrono(pacientes):
        await asyncio.gather(*(diagnostico_asincrono(p) for p in pacientes))

    # En main, llamamos:
# asyncio.run(ejecutar_diagnostico_asincrono(pacientes))

if __name__ == "__main__":
    main()
