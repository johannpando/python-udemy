import shutil
import os

carpeta_origen = 'carpeta_origen'

archivo_destino = "./carpeta_origen/comprimido_con_shutil"
shutil.make_archive(archivo_destino, 'zip', carpeta_origen)

shutil.unpack_archive(archivo_destino + '.zip', './carpeta_destino')


def vaciar_carpeta(ruta_carpeta):
    try:
        # Iterar sobre los archivos y subcarpetas en la carpeta
        for nombre in os.listdir(ruta_carpeta):
            ruta_completa = os.path.join(ruta_carpeta, nombre)
            # Si es un archivo, eliminarlo
            if os.path.isfile(ruta_completa):
                os.remove(ruta_completa)
            # Si es una carpeta, eliminarla recursivamente
            elif os.path.isdir(ruta_completa):
                # os.rmdir(ruta_completa)  # Esta línea solo elimina carpetas vacías
                # Para eliminar una carpeta no vacía, puedes usar shutil.rmtree(ruta_completa)
                shutil.rmtree(ruta_completa)

        print(f"La carpeta '{ruta_carpeta}' ha sido vaciada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# vaciar_carpeta("./carpeta_destino")
