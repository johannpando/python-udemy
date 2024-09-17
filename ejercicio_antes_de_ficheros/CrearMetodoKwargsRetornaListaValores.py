def lista_atributos(**kwargs):
    valores = list(kwargs.values())
    return valores


mi_diccionario = {'x': 1, 'y': 2}
print(lista_atributos(**mi_diccionario))