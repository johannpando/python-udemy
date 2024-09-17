import re


def verificar_email(email):
    expresion = r'^[^@]+@[^@]+\.(com|com\.[a-zA-Z]{2})$'
    if re.match(expresion, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


"""
Crea una función llamada verificar_saludo 
para verificar si una frase entregada como argumento inicia con la palabra "Hola".
"""


def verificar_saludo(frase):
    patron = r'^Hola'
    if re.match(patron, frase):
        print("Ok")
    else:
        print("No has saludado")


"""
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos 
y cuatro numéricos a continuación (ejemplo: XX1234). 
Crea una función, llamada verificar_cp para comprobar si el código postal pasado 
como argumento sigue este patrón. 
Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: 
"El código postal ingresado no es correcto".
"""


def verificar_cp(cp):
    patron = r'\w{2}\d{4}'
    if re.match(patron, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")
