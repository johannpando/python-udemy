class Perro:
    cantidad_perros = 0  # Atributo de clase, compartido por todas las instancias

    def __init__(self, nombre):
        self.nombre = nombre
        Perro.cantidad_perros += 1  # Incrementar el atributo de clase

    @classmethod
    def perros_totales(cls, otro_atributo):  # Método de clase
        print(otro_atributo)
        # A través de un método de clase puedo acceder a un atributo de clase
        # cls.cantidad_perros += 20 # incluso puedo modificar el atributo de clase
        return f"Total de perros: {cls.cantidad_perros}"


# Crear varias instancias de Perro
perro1 = Perro("Firulais")
perro2 = Perro("Bobby")

# Llamar al método de clase
print(Perro.perros_totales('otro_atributo'))  # Total de perros: 2
