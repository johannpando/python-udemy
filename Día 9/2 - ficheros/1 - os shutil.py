import os
import shutil


# Imprime el directorio actual
print(os.getcwd())


# Método walk
ruta = os.getcwd()
print(f"ruta actual es {ruta}")

for carpeta, subcarpeta, archivo in os.walk(ruta):
    print(f"En la carpeta: {carpeta}")
    print(f"Las subcarpetas son: ")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print("Los archivos son: ")
    for arch in archivo:
        print(f"\t{arch}")
    print("\n")

# Crea un dichero
nombre_archivo = 'texto.txt'
archivo = open(nombre_archivo, 'w')
archivo.write('Texto de prueba')
archivo.close()

# Muevo el fichero

# Crear la nueva carpeta_origen si no existe
nueva_carpeta = 'nueva_carpeta'
if not os.path.exists(nueva_carpeta):
    os.makedirs(nueva_carpeta)

# Ruta destino (nueva carpeta_origen) donde se moverá el fichero
ruta_destino = os.path.join(nueva_carpeta, nombre_archivo)

shutil.move(nombre_archivo, ruta_destino)

