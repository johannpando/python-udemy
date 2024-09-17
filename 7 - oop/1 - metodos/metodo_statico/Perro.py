class Perro:
    def __init__(self, nombre):
        self.nombre = nombre

    @staticmethod
    def sonido_comun():  # Método estático
        # no puedo acceder a los atributos de clase ni de instancia
        # cls.nombre
        # self.nombre
        return "Los perros comúnmente ladran"

# Crear una instancia
perro = Perro("Rex")

# Llamar al método estático
print(Perro.sonido_comun())  # Los perros comúnmente ladran
