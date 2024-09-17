mi_archivo = open("texto.txt")
print(mi_archivo.read())

# readline imprime el salto de línea
una_linea = mi_archivo.readline()
print(una_linea)
# para evitar el salto de línea
una_linea = mi_archivo.readline()
print(una_linea.rstrip())
una_linea = mi_archivo.readline()
print(una_linea.rstrip())

print("Cierre primer ejercicio")
# También puedo recorrer las líneas con un for
mi_archivo.close()
"""
otro_archivo = open("otro_fichero_sin_espacios_entre_lineas.txt")

for linea in otro_archivo:
    print(linea)

print("Cierre ejemplo for\n")

# Cuidado con este método y ficheros grandes
todas = otro_archivo.readlines()
print(todas)

otro_archivo.close()
"""
nombre_archivo = "otro_fichero_sin_espacios_entre_lineas.txt"

# Con try with nos aseguramos de cerrar el fichero abierto
try:
    with open(nombre_archivo, 'r', encoding='utf-8') as archivo:
        todas = archivo.readlines()
    print(todas)
except FileNotFoundError:
    print(f"El archivo {nombre_archivo} no se encontró.")
except IOError:
    print(f"Hubo un error al intentar leer el archivo {nombre_archivo}.")

