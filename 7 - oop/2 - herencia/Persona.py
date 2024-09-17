class Persona:

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def establecer_apodo(self, apodo):
        print(f"El apodo de {self.nombre} es {apodo}")


class Alumno(Persona):
    def __init__(self, nombre, edad, numero_matricula):
        # Invoca al constructor de la superclase
        super().__init__(nombre, edad)
        # self.nombre = nombre
        # self.edad = edad
        self.numero_matricula = numero_matricula

    # La clase hija puede tener sus propios métodos
    def establecer_tutor(self, nombre_tutor):
        print(f"El nombre del tutor asignado es {nombre_tutor}")

    # La clase hija también puede sobreescribir los métodos de su clase padre
    def establecer_apodo(self, apodo):
        print(f"Todos los alumnos tienen el apodo de {apodo}")


johann = Alumno("Johann", 20, 12345)
johann.establecer_tutor("Julio")
johann.establecer_apodo("cachimbo")

persona_generic = Persona("Julián", 29)
persona_generic.establecer_apodo("genérico")