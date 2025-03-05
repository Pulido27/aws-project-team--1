from pathlib import Path

indices = {}
separador = chr(31)
with open("Titulos","rb") as archivo:
    pos = archivo.tell() # Obtener la posicion del puntero de lectura
    
    char = "a"
    while char :
        archivo.seek(pos)
        linea = archivo.readline().decode("utf-8")
        data = linea.split(separador) 
        indices[data[0]] = pos
        pos = archivo.tell()
        char = archivo.read(1)