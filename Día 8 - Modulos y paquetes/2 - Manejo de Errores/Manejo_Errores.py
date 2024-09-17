def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
        print("Abriendo exitosamente")
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    finally:
        print("Finalizando ejecución")
