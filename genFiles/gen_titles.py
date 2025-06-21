
import json
from pathlib import Path

# Convierte la ruta en un objeto Path
ruta = Path("/home/ubuntu/internet_archive")
titulo = ""

# Usamos el carácter ASCII 31 (Unit Separator) como separador
separador = chr(31)

with open("Titulos","w",encoding="utf-8") as archivo:

    # Itera la ruta con los archivos dentro
    for carpeta in ruta.iterdir():
        #se valida que sea un directorio
        if carpeta.is_dir():
            #Guardar la  ruta del json
            ruta_json = carpeta / "metadata.json"
            #abrimos el archivo
            with ruta_json.open("r",encoding="utf-8") as archivo_json : 
                # Json ahora como un diccionario (objeto Python)
                archivo_json_string = archivo_json.read()
                metadata_json = json.loads(archivo_json_string)
                #Se extrae el titulo
                titulo = metadata_json["title"]
                #Se extrae el autor
                if("creator" in metadata_json):
                    if isinstance(metadata_json["creator"], str):
                        autor = [metadata_json["creator"]]
                    else :
                        autor = metadata_json["creator"]
                else:
                    autor = ["NULL"]
                #Se escribe el titulo en el txt y salta la linea
                archivo.write(titulo + separador + separador.join(autor) + "\n")