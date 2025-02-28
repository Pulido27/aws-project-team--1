import pytest
from pathlib import Path

def test_numTitulos():
    # Numero de libros procesados (esperados)
    numeroTitulos = 91
    
    with open("../Titulos", "r") as archivo:
        # Numero de libros procesados
        lineas = archivo.readlines()
        print(f"El archivo tiene {len(lineas)} líneas")
        # Compara el numero de titulos esperado con numero de libros que debe de haber
        assert len(lineas) == numeroTitulos 
        
def test_palabraExiste():
    return
