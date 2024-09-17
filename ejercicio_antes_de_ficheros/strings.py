abecedario = "ABCDEFGHIJKLMNÑOPQRSTUVWZ"

# cadena.index(subcadena, start, end)

# Imprime el índice del primer carácter encontrado en el rango de 0 a 2
print(abecedario.index("A", 0, 3))  # Busca la letra "A" en el rango 0 a 3

# Si deseas imprimir los índices de cada letra en el rango 0 a 2
for i in range(3):
    print(f"Índice de {abecedario[i]} es {i}")


# Rangos
# Empieza en el índice 2 hasta el 4 (último no incluido)
fragmento = abecedario[2:4]
print(fragmento)

# Empieza en el índice 2 hasta el 20 (último no incluido) y salta cada dos elementos (tercer argumento)
# cadena[start:stop:step]
# start es el índice inicial del corte (incluido).
# stop es el índice final del corte (no incluido).
# step es el tamaño del paso.
fragmento = abecedario[2:20:2]
print(fragmento)

# Imprime los caracteres de tres en tres
fragmento = abecedario[::3]
print(fragmento)

# Imprime los caracteres al revés, el tercer argumento no puede ser cero
fragmento = abecedario[::-1]
print(fragmento)

frase = "Controlar la complejidad es la esencia de la programación"
extracto = frase[:9]
print(extracto)



####################

frase = "Si la implementación es difícil de explicar, puede que sea una mala idea."
nuevo = frase.replace("difícil", "fácil")
nuevo = nuevo.replace("mala", "buena")
print(nuevo)