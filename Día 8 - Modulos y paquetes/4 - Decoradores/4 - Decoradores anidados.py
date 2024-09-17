"""
Puedes anidar decoradores, aplicando varios a una misma función.
El orden en el que los apliques afectará el comportamiento.
"""


def decorador1(funcion_original):
    def nueva_funcion():
        print("Decorador 1 antes")
        funcion_original()
        print("Decorador 1 después")
    return nueva_funcion


def decorador2(funcion_original):
    def nueva_funcion():
        print("Decorador 2 antes")
        funcion_original()
        print("Decorador 2 después")
    return nueva_funcion


@decorador1
@decorador2
def funcion_a_decorar():
    print("Esta es la función original.")


funcion_a_decorar()


# Salida esperada
"""
Decorador 1 antes
Decorador 2 antes
Esta es la función original.
Decorador 2 después
Decorador 1 después
"""
