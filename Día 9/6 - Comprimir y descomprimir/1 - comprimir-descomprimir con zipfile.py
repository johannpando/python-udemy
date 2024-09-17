import zipfile
import os

mi_zip = zipfile.ZipFile('archivo_comprimido.zip', 'w')
mi_zip.write('texto1.txt')
mi_zip.write('texto2.txt')
mi_zip.close()

try:
    os.remove('texto1.txt')
    os.remove('texto2.txt')
except FileNotFoundError:
    print("Los ficheros no pudieron ser borrados")
else:
    print("Archivos borrados con éxito luego de haber sido comprimidos")


abrir_zip = zipfile.ZipFile('archivo_comprimido.zip', 'r')
abrir_zip.extractall()

