from pyparsing import Word, alphas, infixNotation, opAssoc, CaselessKeyword
import logging
import struct
from pathlib import Path

#Funcion para extraer la informacion de los archivos de palabras .bin
def extraer_indices_binarios(palabra, carpeta_lib):
    # Path del archivo con las posiciones binarios
    archivo = carpeta_lib / palabra
    datos_binarios = []
    
    if not archivo.is_file():
        return []
    
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

NOT = CaselessKeyword("NOT").setParseAction(lambda: 1)
AND = CaselessKeyword("AND").setParseAction(lambda: 2)
OR  = CaselessKeyword("OR").setParseAction(lambda: 3)

# Definición de la gramática de pyparsin : operacion , opeardores , asociatividad
variable = Word(alphas)
expr = infixNotation(variable, [
    (NOT, 1, opAssoc.RIGHT),
    (AND, 2, opAssoc.LEFT),
    (OR,  2, opAssoc.LEFT),
])

def bookSearch(string):

    parsed = expr.parseString(string)
    
    # Convertir a lista de Python
    tree = parsed.asList()
    bin_pos = evaluate_ast(tree)
    
    books = []
     
    with open("TitulosPrueba", "r") as fin:
        for bloque in bin_pos:
            # desempaquetar offset (little-endian unsigned int)
            offset = struct.unpack('<I', bloque)[0]
            fin.seek(offset)
            linea = fin.readline().rstrip('\n')
            linea = linea.split(chr(31))[0]
            books.append(linea)
            
    return books


# Función de evaluación recursiva
def evaluate_ast(node):
    
    if len(node) == 1:
        return evaluate_ast(node[0])

    # caso string (literal)
    if isinstance(node, str):
        return extraer_indices_binarios(node, Path("/home/ubuntu/python_code/work/bookSearcher/test/lib_pruebas"))

    # operador unario
    if node[0] == 1:
        operand = node[1]
        sub = evaluate_ast(operand)
        universo = extraer_indices_binarios("posPrueba.bin", Path("/home/ubuntu/python_code/work/bookSearcher/test"))
        return list(set(universo) - set(sub))

    # operador binario
    left, op, right = node
    L = set(evaluate_ast(left))
    R = set(evaluate_ast(right))
    if op == 2:
        return list(L & R)
    else:
        return list(L | R)
        