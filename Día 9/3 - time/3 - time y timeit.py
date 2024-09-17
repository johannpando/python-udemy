import timeit


# Método 1: Usando un bucle for
def suma_bucle(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total


# Método 2: Usando la fórmula de la suma de una serie
def suma_formula(n):
    return n * (n + 1) // 2


# Número de veces que se ejecutarán las pruebas
numero_de_ejecuciones = 10000
n = 1000  # Número hasta el cual queremos sumar

# Medir el tiempo del primer método
tiempo_bucle = timeit.timeit('suma_bucle(n)', globals=globals(), number=numero_de_ejecuciones)

# Medir el tiempo del segundo método
tiempo_formula = timeit.timeit('suma_formula(n)', globals=globals(), number=numero_de_ejecuciones)

# Imprimir resultados
print(f"Tiempo usando bucle for: {tiempo_bucle:.6f} segundos")
print(f"Tiempo usando fórmula: {tiempo_formula:.6f} segundos")
