def suma_menores(lista):
    lista_numeros = 0
    for n in lista:
        if n > 0 and n < 1000:
            lista_numeros = lista_numeros + n

    return lista_numeros


lista_numeros = [1, 2, 1000, 4]

print(suma_menores(lista_numeros))