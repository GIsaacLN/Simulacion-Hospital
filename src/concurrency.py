import threading
import queue
from utils import registro, seguimiento_y_alta
import logging

def diagnostico(paciente):
    logging.info(f"Diagnóstico síncrono de {paciente}")
    import time; time.sleep(0.2)

def asignar_cama(paciente):
    logging.info(f"Asignando cama a {paciente}")
    import time; time.sleep(0.1)

def atender_paciente(paciente_queue, cama_sema):
    while True:
        paciente = paciente_queue.get()
        if paciente is None:
            paciente_queue.task_done()
            break
        registro(paciente)
        diagnostico(paciente)
        with cama_sema:
            asignar_cama(paciente)
            seguimiento_y_alta(paciente)
        paciente_queue.task_done()

def lanzar_concurrencia(num_pacientes=10, num_enfermeros=5):
    paciente_queue = queue.Queue()
    cama_sema = threading.Semaphore(3)  # Camas disponibles

    # Iniciar hilos
    threads = []
    for _ in range(num_enfermeros):
        t = threading.Thread(target=atender_paciente, args=(paciente_queue, cama_sema))
        t.daemon = True
        t.start()
        threads.append(t)

    # Generar y encolar pacientes
    from utils import generar_pacientes
    for p in generar_pacientes(num_pacientes):
        paciente_queue.put(p)

    # Esperar a que terminen
    paciente_queue.join()

    # Detener hilos
    for _ in threads:
        paciente_queue.put(None)
    for t in threads:
        t.join()
