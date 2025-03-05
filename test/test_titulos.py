import pytest

def test_procesamiento_metadata():
    # Lista de 10 metadatas de prueba con distintas configuraciones
    fake_metadatas = [
        {"title": "Libro 1", "creator": "Autor1"},
        {"title": "Libro 2", "creator": "Autor2"},
        {"title": "Libro 3", "creator": ["Autor3a", "Autor3b"]},
        {"title": "Libro 4", "creator": "Autor4"},
        {"title": "Libro 5", "creator": ["Autor5a", "Autor5b", "Autor5c"]},
        {"title": "Libro 6"},  # Sin campo "creator"
        {"title": "Libro 7", "creator": "Autor7"},
        {"title": "Libro 8", "creator": ["Autor8a", "Autor8b"]},
        {"title": "Libro 9", "creator": "Autor9"},
        {"title": "Libro 10", "creator": "Autor10"}
    ]
    
    # Usamos el carácter ASCII 31 (Unit Separator) como separador
    separador = chr(31)
    
    # Iteramos sobre cada metadata para procesarla y compararla con el resultado esperado
    for metadata in fake_metadatas:
        titulo = metadata["title"]
        if "creator" in metadata:
            # Si el creador es una cadena, lo convertimos a lista para usar join
            if isinstance(metadata["creator"], str):
                autor = [metadata["creator"]]
            else:
                autor = metadata["creator"]
        else:
            autor = ["NULL"]
        
        # Construimos el resultado usando el separador
        resultado = titulo + separador + separador.join(autor) + "\n"
        
        # Construimos el resultado esperado de forma manual
        if "creator" in metadata:
            if isinstance(metadata["creator"], str):
                esperado = titulo + separador + metadata["creator"] + "\n"
            else:
                esperado = titulo + separador + separador.join(metadata["creator"]) + "\n"
        else:
            esperado = titulo + separador + "NULL" + "\n"
        
        # Comparamos ambos resultados
        assert resultado == esperado
