###################
# Lista de palabras
palabras = ["Hola", "mundo", "Python", "es", "genial"]

# Unir las palabras con un espacio
frase = " ".join(palabras)
print(frase)  # Salida: Hola mundo Python es genial

# Unir las palabras con una coma
frase_coma = ", ".join(palabras)
print(frase_coma)  # Salida: Hola, mundo, Python, es, genial

palabras.append("Adiós")
print(palabras)

frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)
print(eliminado)