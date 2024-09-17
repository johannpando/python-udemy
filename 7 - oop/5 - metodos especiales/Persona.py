class Persona:

    def __init__(self, nombre):
        self.nombre = nombre


# Si intentamos imprimir la función "len" de nuestro objeto nos va a devolver un error
p = Persona("Johann")


# print(len(p))
# TypeError: object of type 'Persona' has no len()

# Podemos redefinir el método len (y otros muchos métodos más) dentro de la misma clase

class Extraterrestre:

    def __init__(self, nombre):
        self.nombre = nombre

    def __len__(self):
        # len es un método que devuelve un número por lo que no podemos redefinirlo como nos de la gana
        # return "La longitud por defecto es interminable" Esto da error
        return 10


it = Extraterrestre("IT")
print(len(it))


class Libro:
    def __init__(self, titulo, autor, cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        print("Libro eliminado")
