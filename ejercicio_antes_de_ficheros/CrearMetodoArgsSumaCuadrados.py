def suma_cuadrados(*args):
    suma = 0
    for n in args:
        # print(type(n))
        # print(n)
        suma += n * n
    return suma


print(suma_cuadrados(1, 2, 3))