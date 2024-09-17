def sobrescribir(archivo):
    fichero = open(archivo, "w")
    fichero.write("contenido eliminado")
    fichero.close()


def registro_error(archivo):
    fichero = open(archivo, "a")
    fichero.write("se ha registrado un error de ejecución")
    fichero.close()