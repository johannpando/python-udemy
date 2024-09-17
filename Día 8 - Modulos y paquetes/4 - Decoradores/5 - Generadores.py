"""
Los generadores en Python son una forma especial de funciones que devuelven una secuencia de valores
de manera "perezosa" (lazy), es decir, van produciendo uno a uno conforme se necesitan en lugar de devolver
toda la secuencia de una vez.
Los generadores se implementan usando la palabra clave yield.
"""


def generador_numeros():
    yield 1
    yield 2
    yield 3


# Creamos el generador
gen = generador_numeros()

# Extraemos los valores uno por uno
print(next(gen))  # Imprime 1
print(next(gen))  # Imprime 2
print(next(gen))  # Imprime 3


# En bucles for no hace falta llamar a next

def generador_numeros():
    yield 1
    yield 2
    yield 3


# Usamos el generador en un bucle for
for numero in generador_numeros():
    print(numero)


# Otros ejemplos de las prácticas

def generador_numeros():
    num = 0
    while True:
        num = num + 1
        yield num


generador = generador_numeros()
