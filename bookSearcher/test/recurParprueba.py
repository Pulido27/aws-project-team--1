from pyparsing import Word, alphas, infixNotation, opAssoc
import logging
import struct
from pathlib import Path

#Funcion para extraer la informacion de los archivos de palabras .bin
def extraer_indices_binarios(palabra, carpeta_lib):
    # Path del archivo con las posiciones binarios
    archivo = carpeta_lib / palabra
    datos_binarios = []
    
    with archivo.open("rb") as f:
        while True:
            bloque = f.read(4)
            if len(bloque) < 4:  # ya no quedan más offsets
                break
            datos_binarios.append(bloque)

    return datos_binarios

# Configuración de logging
logger = logging.getLogger(__name__)
logging.basicConfig()
logger.setLevel(logging.DEBUG)

# Definición de la gramática de pyparsin : operacion , opeardores , asociatividad
variable = Word(alphas)
expr = infixNotation(variable, [
    ("NOT", 1, opAssoc.RIGHT),
    ("AND", 2, opAssoc.LEFT),
    ("OR",  2, opAssoc.LEFT),
])

# 1) Parsear la expresión
parsed = expr.parseString("suenoz OR vida")

# 2) Convertir a lista de Python
tree = parsed.asList()

# 3) Si es lista de un solo elemento, desempaquetar
if isinstance(tree, list) and len(tree) == 1:
    tree = tree[0]

# 4) Leer universo completo de offsets
UNIVERSO = extraer_indices_binarios("posPrueba.bin", Path("/home/ubuntu/python_code/work/bookSearcher/test"))

# Función de evaluación recursiva
def evaluate_ast(node, universo):
    # caso lista de un solo elemento: desempaqueta
    if isinstance(node, list) and len(node) == 1:
        return evaluate_ast(node[0], universo)

    # caso string (literal)
    if isinstance(node, str):
        return extraer_indices_binarios(node, Path("/home/ubuntu/python_code/work/bookSearcher/test/lib_pruebas"))

    # operador unario
    if isinstance(node, list) and len(node) == 2:
        op, operand = node
        sub = evaluate_ast(operand, universo)
        if op == 'NOT':
            return list(set(universo) - set(sub))
        logger.error(f"Operador unario desconocido: {op}")
        return []

    # operador binario
    if isinstance(node, list) and len(node) == 3:
        left, op, right = node
        L = set(evaluate_ast(left, universo))
        R = set(evaluate_ast(right, universo))
        if op == 'AND':
            return list(L & R)
        if op == 'OR':
            return list(L | R)
        logger.error(f"Operador binario desconocido: {op}")
        return []

    logger.error(f"Nodo inválido: {node}")
    return []

# 5) Evaluar el AST
resultados = evaluate_ast(tree, UNIVERSO)

# 6) Recuperar y mostrar líneas desde "TitulosPrueba"
with open("TitulosPrueba", "r") as fin:
    for bloque in resultados:
        # desempaquetar offset (little-endian unsigned int)
        offset = struct.unpack('<I', bloque)[0]
        fin.seek(offset)
        linea = fin.readline().rstrip('\n')
        print(linea)
