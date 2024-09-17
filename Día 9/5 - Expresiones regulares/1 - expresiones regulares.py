import re

texto = 'Si necesitas ayuda llama al (658)-677-8989 las 24 horas del día, ayuda online'

palabra_a_buscar = 'ayuda'

palabra = palabra_a_buscar in texto
print(palabra)  # Imprime True

busqueda = re.search(palabra_a_buscar, texto)
print(busqueda)
# Imprime un objeto de tipo Match
# <re.Match object; span=(13, 18), match='ayuda'>
print(busqueda.span())  # Imprime 13, 18

# La palabra ayuda se incluye en 'texto' más de una vez
print(re.findall(palabra_a_buscar, texto))  # Imprime ['ayuda', 'ayuda']

# También podemos interar con finditer, devuelve un objeto Match
for p in re.finditer(palabra_a_buscar, texto):
    print(p)

# Expresiones regulares
expresion = r'\(\d\d\d\)-\d\d\d-\d\d\d\d'
resultado = re.search(expresion, texto)
print(resultado)
# Imprime <re.Match object; span=(28, 42), match='(658)-677-8989'>
print(resultado.group())  # Imprime el número
expresion_mejorada = r'\(\d{3}\)-\d{3}-\d{4}'
resultado = re.search(expresion_mejorada, texto)
print(resultado)
# Imprime <re.Match object; span=(28, 42), match='(658)-677-8989'>
print('*' * 23)
# expresion_mejorada_compile = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4)')
expresion_mejorada_compile = re.compile(r'(\(\d{3}\))-(\d{3})-(\d{4})')
resultado = re.search(expresion_mejorada_compile, texto)
print(resultado.group(2))  # Imprime 677

# Cuantificadores

# clave = input("Clave: ")
clave = "e1a2b3cf"
# La clave debe seguir el patrón: primer dígito no numérico luego 7 caracteres alfanuméricos. Por ejemplo: e1a2b3cf
patron = r'\D{1}\w{7}'
verificar = re.search(patron, clave)
print(verificar)  # Imprime un objeto Match de lo contrario None

texto = "lunes, martes y miércoles"
patron = re.search(r'lunes|martes', texto)
print(patron)
