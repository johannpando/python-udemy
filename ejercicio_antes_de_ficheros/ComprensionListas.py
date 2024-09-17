# Método actual
palabra = 'python'
lista = []
for letra in palabra:
    lista.append(letra)
print(lista)

# Aplicando comprensión de listas
# Una letra por cada letra dentro de la lista palabra
lista_nueva = [letra for letra in palabra]
print(lista_nueva)

# Añadiendo if
lista_nueva2 = [n + 1 for n in range(0, 21, 2) if n == 10]
# Imprime 11
print(lista_nueva2)

# Añadiendo else
lista_nueva3 = [n if n == 10 else 'no' for n in range(0, 21, 2)]
# Imprime ['no', 'no', 'no', 'no', 'no', 10, 'no', 'no', 'no', 'no', 'no']
print(lista_nueva3)

# Valores al cuadrado
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [n * n for n in valores]

# Pares
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_pares = [n for n in valores if n % 2 == 0]

# Celsius
temperatura_fahrenheit = [32, 212, 275]

grados_celsius = [(t - 32) * (5 / 9) for t in temperatura_fahrenheit]
