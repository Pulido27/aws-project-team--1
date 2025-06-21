import pytest
from pathlib import Path

def test_librosEncontrados():
    palabrasManual = set([
    "acelerava", "alba", "caia", "ciud", "dela", "enel", "entre", "eria", "hastaque",
    "llegava", "logica", "mezclava", "muros", "noche", "pegadas", "porque", "realid",
    "sombr", "sucesion", "surgian", "todo", "unqq",
    "alaescuchar", "bras", "caos", "convertia", "donde", "entender", "enun", "habiauna",
    "ilusiones", "lluvia", "magia", "mundo", "nava", "palabras", "podia", "principe",
    "sobre", "staque", "suenoz", "susurro", "unian", "vida"
    ])
    
    ruta = Path("/home/ubuntu/python_code/work/test/lib_pruebas")
    
    for libs in ruta.iterdir():
        if libs.name != ".pytest_cache":
            assert libs.name in palabrasManual
            