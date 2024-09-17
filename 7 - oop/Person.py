class Person:

    # Atributos de clase
    soul = True

    # Atributos de instancia
    # Constructor
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    # Métodos
    def puede_conducir(self, valor):
        puede = "no"
        if valor:
            puede = "sí"

        # Puedo invocar a los atributos de clase debido a que todos los métodos llevan la instancia de la clase
        # en el método
        print(f'{self.name} {puede} puede conducir')


myPerson = Person("Johann", "Pando")
print(myPerson.name)
print(myPerson.last_name)

print(f'Mi nombre es {myPerson.name} y mi apellido es {myPerson.last_name} y mi alma es {myPerson.soul}')
print(myPerson.puede_conducir(True))