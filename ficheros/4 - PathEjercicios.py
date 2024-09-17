from pathlib import Path
import os

base = Path.home()
ruta = Path(base, "ruta", "otra_ruta")

print(ruta)

# parent se puede concatenar

print(ruta.parent.parent)

# podemos iterar para buscar por extensión de fichero, por ejemplo:

ruta_actual = os.getcwd()

for extension_python in Path(ruta_actual).glob("*.py"):
    print(extension_python)

print("\n\n\n")

# podemos hacer que sea recursivo

for fichero in Path(ruta_actual).glob("**/*.py"):
    print(fichero)

print("\n\n\n")

ruta_relativa = Path("Europa", "España", "Las Palmas", "Las Canteras")
en_europa = ruta_relativa.relative_to(Path("Europa"))
print(en_europa)
# Esto no funciona
# en_las_palmas = ruta_relativa.relative_to(Path("Europa", "Las Palmas"))
en_las_palmas = ruta_relativa.relative_to(Path("Europa", "España"))
print(en_las_palmas)

# Crear una ruta absoluta

ruta = Path.home() / Path("Curso Python", "Día 6", "practicas_path.py")