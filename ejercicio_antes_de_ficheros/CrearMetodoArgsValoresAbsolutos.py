def suma_absolutos(*args):
    suma = 0
    for n in args:
        # El método abs quita el signo del número convirtiéndolo a positivo
        suma += abs(n)

    return suma


print(suma_absolutos(1, -2, -3))