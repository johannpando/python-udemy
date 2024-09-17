def contar_primos(num):
    contador = 0
    list_primos = []

    for n in range(2, num + 1):
        if n > 1:
            for f in range(2, n):
                if n % f == 0:
                    break
            else:
                contador += 1
                list_primos.append(n)

    print(list_primos)
    return contador


print(contar_primos(4))
