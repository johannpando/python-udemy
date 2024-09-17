"""
Python nos proporciona una sintaxis más simple para aplicar decoradores usando @.
Así no tienes que asignar manualmente el decorador a la función.
"""


# Definimos el decorador
def decorador(funcion_original):
    def nueva_funcion():
        print("Código antes de la función original.")
        funcion_original()
        print("Código después de la función original.")
    return nueva_funcion


# Aplicamos el decorador con la sintaxis @
@decorador
def funcion_a_decorar():
    print("Esta es la función original.")


# Ahora llamamos la función decorada
funcion_a_decorar()
