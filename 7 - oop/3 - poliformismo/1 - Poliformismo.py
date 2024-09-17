class Perro:
    def hacer_sonido(self):
        return "El perro ladra"


class Gato:
    def hacer_sonido(self):
        return "El gato maúlla"


# Función que utiliza polimorfismo
def escuchar_animal(animal):
    print(animal.hacer_sonido())


# Crear instancias de las clases
mi_perro = Perro()
mi_gato = Gato()

# Usar la misma función para diferentes tipos de objetos
escuchar_animal(mi_perro)  # El perro ladra
escuchar_animal(mi_gato)  # El gato maúlla
