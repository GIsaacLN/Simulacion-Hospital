# Hospital Simulation

Proyecto de simulación de un sistema hospitalario automatizado integrando concurrencia, paralelismo y asincronía.

## Requisitos

- Python 3.10+
- Librerías:

  - `aiohttp`
  - `numpy`
  - `psutil`
  - `pytest`
  - `pytest-asyncio`

## Instalación

```bash
git clone https://github.com/GIsaacLN/hospital_simulation.git
cd hospital_simulation
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install -r requirements.txt
```

> El flag `-e` en `pip install -e .` instala tu paquete en modo editable, de modo que puedas importar `src.*` sin configurar `PYTHONPATH`.

## Estructura del proyecto

```
.
├── src/                    ← Código fuente
│   ├── __init__.py
│   ├── async_tasks.py
│   ├── concurrency.py
│   ├── main.py
│   ├── parallel.py
│   └── utils.py
├── tests/                  ← Test suite
│   ├── __init__.py
│   ├── test_async.py
│   ├── test_concurrency.py
│   └── test_parallel.py
├── .vscode/                ← Configuración de VS Code
│   ├── launch.json
│   └── settings.json
├── .venv/                  ← Entorno virtual (gitignored)
├── requirements.txt
├── setup.py
├── README.md
└── resultados_tests.txt    ← Salida de `pytest`
```

## Uso

### Ejecutar la simulación

```bash
python src/main.py
```

### Ejecutar pruebas

```bash
pytest --maxfail=1 --disable-warnings -q --durations=5
```

Si quieres además guardar la salida en un archivo:

```bash
pytest --maxfail=1 --disable-warnings -q --durations=5 | tee resultados_tests.txt
```
