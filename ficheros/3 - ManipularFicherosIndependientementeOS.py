import os
from pathlib import Path

# Imprime el directorio actual
donde_estoy = os.getcwd()
print(donde_estoy)

# La barra / se usa independientemente del sistema operativo
carpeta = Path('/Users/johannpando/PycharmProjects/pythonProject/ficheros')
# Además se usa para concatenar carpetas y/o nombres de ficheros
archivo = carpeta / "texto.txt"

archivo_final = open(archivo)
print(archivo_final.read())

# Con Path no hace falta ni abrir el fichero ni cerralo

fichero_path = Path('/Users/johannpando/PycharmProjects/pythonProject/ficheros/texto.txt')
print(fichero_path.read_text())