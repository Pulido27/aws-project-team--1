📚 Buscador de Palabras en Libros
Aplicación para buscar una palabra o conjunto de palabras y descubrir en qué libros aparecen. Ideal para investigadores, lectores curiosos o cualquier persona que necesite rastrear términos específicos en una colección de textos.

📁 Estructura del Proyecto
El proyecto está dividido en dos módulos principales:

genfiles/: Generación de archivos binarios optimizados para la búsqueda.

bookSearcher/: Lógica del motor de búsqueda.

⚙️ genfiles – Generador de Índices
Este módulo se encarga de preparar los datos para permitir búsquedas rápidas y eficientes.

Pasos para generar los archivos:
gen_titles.py
Genera el archivo Titulos.txt con los títulos de los libros.

gen_index.py
Usa Titulos.txt para generar archivos .bin en la carpeta files_bin/, que contienen los índices de palabras.

gen_posBin.py
Crea el archivo pos.bin, que almacena las posiciones de inicio de cada línea en Titulos.txt para una recuperación rápida.

Nota:
El script gen_dic.py es una dependencia interna de gen_index.py y no necesita ejecutarse manualmente. Su función es mapear los títulos con sus posiciones en el archivo.

🔍 bookSearcher – Motor de Búsqueda
Este módulo permite realizar búsquedas sobre los archivos generados.

Uso principal
recurPar.py
Ejecuta este script para buscar palabras y obtener una lista de los libros donde aparecen.

Pruebas
La carpeta test/ contiene pruebas para validar el sistema:

recurPar_Prueba.py
Versión de prueba de recurPar.py con rutas simplificadas para testeo.

test_libros.py
Pruebas unitarias desarrolladas con pytest para verificar la lógica del motor de búsqueda.

main.py:
El archivo main.py permite ejecutar búsquedas directamente desde la consola.