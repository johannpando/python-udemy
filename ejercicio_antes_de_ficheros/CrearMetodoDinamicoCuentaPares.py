def cantidad_pares(lista):
    lista_numeros = 0
    for n in lista:
        if n % 2 == 0:
            lista_numeros += 1

    return lista_numeros


lista_a_probar = [1, 2, 3, 4]

print(cantidad_pares(lista_a_probar))
