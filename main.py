#from bookSearcher.recurPar import bookSearch
from bookSearcher import bookSearch
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        expresion = " ".join(sys.argv[1:])
        bookSearch(expresion)
    else:
        while True:
            expresion = input("Ingresa tu expresión (o 'q'):\n> ")
            if expresion.lower() == "q":
                break
            try:
                bookSearch(expresion)
            except Exception as e:
                print("Error al procesar la expresión:", e)
