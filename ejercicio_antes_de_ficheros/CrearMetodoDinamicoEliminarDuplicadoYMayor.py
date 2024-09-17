def reducir_lista(lista):
    # Set no permite duplicados por lo que podemos convertir de list a set
    lista_sin_duplicados = list(set(lista))
    # La función max devuelve el número más alto
    valor_mas_alto = max(lista_sin_duplicados)
    # Eliminamos de la lista (sin duplicados) el valor más alto
    lista_sin_duplicados.remove(valor_mas_alto)
    return lista_sin_duplicados


def promedio(lista):
    # La función sum suma todos los elementos de la lista
    suma_total = sum(lista)
    # La función len recupera el total de elementos
    numero_de_elementos = len(lista)
    # Calculamos y retornamos el promedio
    calculo_promedio = suma_total / numero_de_elementos
    return calculo_promedio


lista_numeros = [1, 1, 2, 5, 9, 10]
print(reducir_lista(lista_numeros))
print(promedio(reducir_lista(lista_numeros)))