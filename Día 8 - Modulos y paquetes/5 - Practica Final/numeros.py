def numeros_perfumeria():
    for n in range(1, 1000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1, 1000):
        yield f"F - {n}"


def numeros_cosmetica():
    for n in range(1, 1000):
        yield f"C - {n}"


p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()


def decorador(tipo):
    print("\n" + "*" * 23)
    print("Su número es: ")
    if tipo == "P":
        print(next(p))
    elif tipo == "F":
        print((next(f)))
    elif tipo == "C":
        print(next(c))
    print("Pronto será atendido")
    print("\n" + "*" * 23)
