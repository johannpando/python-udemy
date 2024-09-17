def imprime_tipo(**kwargs):
    print(type(kwargs))
    total = 0
    # Recuerda recuperar los items para que funcione el desempaquetado de clave y valor
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")
        total += valor
    return total


print(imprime_tipo(x=1, y=2))


# Cuidado, *args y **kwargs deben ir en último valor
def imprime_varios_tipos(num1, num2, *args, **kwargs):
    print(f"La suma de {num1} y {num2} es: {num1 + num2}")

    for n in args:
        print(f"valor de lista en el índice {args.index(n)} es: {n}")

    total = 0
    # Recuerda recuperar los items para que funcione el desempaquetado de clave y valor
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")
        total += valor
    return total


lista_numeros = [1, 2, 3]
mi_diccionario = {'x': 1, 'y': 2}
print(imprime_varios_tipos(1, 2, *lista_numeros, **mi_diccionario))
