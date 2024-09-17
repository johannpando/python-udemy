from random import choice


def lanzar_moneda():
    cara_o_cruz = ['Cara', 'Cruz']
    return choice(cara_o_cruz)


def probar_suerte(resultado_moneda, lista):
    if resultado_moneda.lower() == 'cara':
        print("La lista se eliminará")
        lista.clear()
        return lista
        # return lista.clear() CUIDADO: El método clear no devuelve la lista vacía, lo hace al vuelo.
        # En este caso retornaría un tipo None
    elif resultado_moneda.lower() == 'cruz':
        print("La lista fue salvada")
        return lista


lista_numeros = [1, 5, 8]

# print(lanzar_moneda())
print(probar_suerte(lanzar_moneda(), lista_numeros))
