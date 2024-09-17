class Persona:
    # Constructor de la clase
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    # Constructor de la clase
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        # Invocamos al constructor de la superclase
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

    # Sobreescribimos el comportamiento del método str para dejar un mensaje genérico
    def __str__(self):
        return f"Cliente: {self.nombre} {self.apellido}\nBalance de cuenta {self.numero_cuenta}: €{self.balance}"

    def depositar(self, monto_deposito):
        self.balance += monto_deposito
        print("Deposito aceptado")

    def retirar(self, monto_retiro):
        if self.balance >= monto_retiro:
            self.balance -= monto_retiro
            print("Retiro realizado")
        else:
            print("Fondo insuficiente")


def crear_cliente():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    numero_cuenta = input("Ingrese su número de cuenta: ")
    cliente = Cliente(nombre, apellido, numero_cuenta)
    return cliente


def inicio():
    mi_cliente = crear_cliente()
    print(mi_cliente)
    option = ''

    while option != 'S':
        print("Elige: Depositar (D), Retirar (R) o Salir (S)")
        option = input().lower()  # Convertimos la entrada a minúsculas

        if option == 'd':
            monto_depositado = int(input("Monto a depositar: "))
            mi_cliente.depositar(monto_depositado)
        elif option == 'r':
            monto_retirar = int(input("Monto a retirar: "))
            mi_cliente.retirar(monto_retirar)
        # Independientemente de la opción mostramos el método str sobreescrito
        print(mi_cliente)
    print("Gracias por operar con nuestro Banco")


# Método que inicia todo el proceso.
inicio()