def todos_positivos(lista):
    alguno_negativo = False
    for n in lista:
        if n < 0:
            alguno_negativo = True
            break

    if alguno_negativo:
        return False
    else:
        return True


lista_numeros = [1, -2, 3]
print(todos_positivos(lista_numeros))
