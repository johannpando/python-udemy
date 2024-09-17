# Métodos de apertura:
# r: read (por defecto)
# w: sobrescribe
# a: añade desde el final
otro_archivo = open("otro_fichero_sin_espacios_entre_lineas.txt", 'r')

# Abro, reemplazo, cierro y leo.
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt")
print(archivo.read())

otro_archivo.close()

# Abre el fichero y al final del contenido se añade el contenido de una lista y por cada ítem se añade un tabulador

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

archivo = open("registro.txt", "a")

for linea in registro_ultima_sesion:
    archivo.write(linea + "\t")

archivo.close()
archivo = open("registro.txt")
print(archivo.read())
