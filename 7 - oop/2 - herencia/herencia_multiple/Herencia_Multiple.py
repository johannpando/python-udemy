class Padre:
    def saludo(self):
        print(f"Soy tu padre")


class Madre:
    def saludo(self):
        print(f"Soy tu madre")


# La clase hijo hereda primero de padre y luego de madre
class Hijo(Padre, Madre):
    pass


class Nieto(Hijo):
    pass


nieto = Nieto()
# Imprimo el orden de la 2 - herencia múltiple
print(Nieto.__mro__)
# (<class '__main__.Nieto'>, <class '__main__.Hijo'>,
# <class '__main__.Padre'>, <class '__main__.Madre'>, <class 'object'>)
nieto.saludo()