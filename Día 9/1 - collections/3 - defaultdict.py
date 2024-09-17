from collections import defaultdict

# Crear un defaultdict con valor predeterminado "Valor no hallado"
mi_diccionario = defaultdict(lambda: 'Valor no hallado')

# Cargar el diccionario con la palabra clave 'edad' y el valor 44
mi_diccionario['edad'] = 44

# Acceder a una clave existente
print(mi_diccionario['edad'])  # Imprimirá 44

# Acceder a una clave inexistente para ver el valor predeterminado
print(mi_diccionario['nombre'])  # Imprimirá "Valor no hallado"
