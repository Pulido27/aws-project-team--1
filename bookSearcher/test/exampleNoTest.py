# from pyparsing import Word, alphas, infixNotation, opAssoc

# variable = Word(alphas) 
# expr = infixNotation(variable, [
#     ("NOT", 1, opAssoc.RIGHT),
#     ("AND", 2, opAssoc.LEFT),
#     ("OR", 2, opAssoc.LEFT)
# ])
 
# result = expr.parseString("p AND q AND c AND y") 

# print(result)

from bookSearcher.readPos import extraer_indices_binarios
from pathlib import Path


print(extraer_indices_binarios("pos.bin", Path("/home/ubuntu/python_code/work/genFiles")))