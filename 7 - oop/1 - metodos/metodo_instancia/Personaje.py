class Personaje:

    # Constructor
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1


"""
Práctica Tipos de Métodos 3
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que tiene una instancia de Personaje, 
que cuenta con un atributo de instancia de tipo número, llamado cantidad_flechas.
"""
