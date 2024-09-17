def numeros_persona(nombre, *args):
    suma_numeros = sum(args)
    return f"{nombre}, la suma de tus números es {suma_numeros}"


print(numeros_persona("Juan", 1, 2, 3))

# Lo siguiente no funciona, para este caso habría que usar **kwargs
# print(numeros_persona("Esteban", x=3, y=2))