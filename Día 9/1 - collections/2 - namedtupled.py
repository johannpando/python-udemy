from collections import namedtuple

# Uso de namedtupled
mi_tupla = (2, 6, 9)
print(mi_tupla[1])  # Imprime 6


"""
Los namedtuple son útiles cuando necesitas estructuras de datos ligeras e inmutables con nombres de campo legibles, 
sin la necesidad de definir una clase completa.
"""
# Definimos el namedtuple
Persona = namedtuple('Persona', ['nombre', 'edad', 'profesion'])

# Creamos una instancia del namedtuple
persona1 = Persona(nombre='Ana', edad=28, profesion='Ingeniera')

# Accedemos a los valores por nombre
print(persona1.nombre)      # Ana
print(persona1.edad)        # 28
print(persona1.profesion)   # Ingeniera
