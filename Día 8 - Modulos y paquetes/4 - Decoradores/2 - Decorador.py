"""
Los decoradores en Python son funciones que permiten modificar o extender el comportamiento de otras funciones o métodos
sin modificar su estructura. Un decorador envuelve una función,
añadiendo lógica antes o después de su ejecución, o incluso reemplazándola.

¿Cómo funcionan los decoradores?
Un decorador es esencialmente una función que toma otra función como argumento y retorna una nueva función.
Esta nueva función normalmente extiende el comportamiento de la función original.

"""


# Definimos el decorador
def decorador(funcion_original):
    def nueva_funcion():
        print("Código que se ejecuta antes de la función original.")
        funcion_original()
        print("Código que se ejecuta después de la función original.")
    return nueva_funcion


# Definimos una función a decorar
def funcion_a_decorar():
    print("Esta es la función original.")


# Usamos el decorador de manera manual
funcion_decorada = decorador(funcion_a_decorar)
funcion_decorada()
