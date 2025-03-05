import pytest
from pathlib import Path

def dividir_carpetas():
    ruta = Path("/home/ubuntu/python_code/work/muestras")
    num_procesos = 2
    carpetas = [carpeta for carpeta in ruta.iterdir() if carpeta.is_dir()]
    tamaño_bloque = len(carpetas) // num_procesos
    partes = [carpetas[i:i + tamaño_bloque] for i in range(0, len(carpetas), tamaño_bloque)]
    print(len(partes))
    if len(partes) > num_procesos:
        partes[-2].extend(partes[-1])
        partes.pop()
    
    assert partes == num_procesos

dividir_carpetas()