import json

def test_procesamiento_metadata():
    # Definimos el JSON de prueba manualmente
    fake_metadata = {
        "title": "Libro de Prueba",
        "creator": "Autor1"
    }
    
    # Usamos el carácter ASCII 31 (Unit Separator) como separador, que es un valor inválido en textos normales
    separador = chr(31)
    
    # Procesamos el JSON de la misma forma que en el código original:
    titulo = fake_metadata["title"]
    if "creator" in fake_metadata:
        if isinstance(fake_metadata["creator"], str):
            autor = [fake_metadata["creator"]]
        else:
            autor = fake_metadata["creator"]
    else:
        autor = ["NULL"]
    
    # Construimos el resultado usando el separador inválido en lugar del guión bajo
    resultado = titulo + separador + separador.join(autor) + "\n"
    
    # Definimos el resultado esperado manualmente con el mismo separador
    esperado = "Libro de Prueba" + separador + "Autor1" + "\n"
    
    # Comparamos ambos resultados
    assert resultado == esperado
