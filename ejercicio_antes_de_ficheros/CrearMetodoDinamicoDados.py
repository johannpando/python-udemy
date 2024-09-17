from random import randint


def lanzar_dados():
    resul1 = randint(1, 6)
    resul2 = randint(1, 6)
    # Devuelve un tuple con dos valores
    return resul1, resul2


def evaluar_jugada(num1, num2):
    suma_dados = num1 + num2
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    # elif suma_dados > 6 and suma_dados < 10:
    elif 6 < suma_dados < 10:
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    elif suma_dados >= 10:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"


# Desempaque de la tuple con *
# El operador * delante de lanzar_dados() se llama operador de desempacado (splat operator).
# Cuando usamos *lanzar_dados(), estamos tomando cada elemento de la tuple
# resultados y pasándolo como un argumento separado a la función evaluar_jugada.
print(evaluar_jugada(*lanzar_dados()))
