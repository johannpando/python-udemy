def convertir(tipo):

    def convertir_mayuscula(texto):
        print(texto.upper())

    def convertir_minuscula(texto):
        print(texto.lower())

    def imprimir_numero_mas_dos(numero):
        print(numero + 2)

    # Comprobar si `tipo` es una cadena
    if isinstance(tipo, str):
        if tipo == "may":
            return convertir_mayuscula
        elif tipo == "min":
            return convertir_minuscula
    # Comprobar si `tipo` es un entero
    elif isinstance(tipo, int):
        return imprimir_numero_mas_dos
    else:
        raise ValueError("Tipo no válido")


# Para cadenas en mayúsculas
operacion = convertir("may")
operacion("texto")  # Imprime "TEXTO"

# Para números
operacion_numero = convertir(4)
operacion_numero(3)  # Imprime 5 (4 + 2)
