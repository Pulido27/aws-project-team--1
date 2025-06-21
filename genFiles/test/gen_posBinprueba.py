import struct

# Abre el archivo "Titulos" en modo binario y crea "pos.bin" para escritura
with open("TitulosPrueba", "rb") as fin, open("posPrueba.bin", "wb") as fout:
    pos = fin.tell()  # posición inicial (0)
    while True:
        # Escribe la posición actual (offset) como entero de 4 bytes
        fout.write(struct.pack("I", pos))
        
        # Lee la siguiente línea; si no hay más, sal del bucle
        linea = fin.readline()
        if not linea:
            break
        
        # Actualiza la posición al byte donde comienza la próxima línea
        pos = fin.tell()
