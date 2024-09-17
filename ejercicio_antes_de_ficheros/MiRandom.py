# No puedo llamar al fichero igual que al módulo a importar

from random import randint
from random import random
from random import choice
from random import shuffle

aleatorio = randint(1, 11)

print(aleatorio)

# Imprime un número decimal aleatorio del 0 al 1
aleatorio = random()
print(aleatorio)

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
# Obtiene un elemento al azar
sorteo = choice(nombres)
print(sorteo)
# Muestra la lista con los elementos ordenados, pero no modifica la lista, lo hace al vuelo
shuffle(nombres)

print(nombres)
