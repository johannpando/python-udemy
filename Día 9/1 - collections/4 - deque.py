"""
Para implementar una deque (doble cola) que inserte elementos por la izquierda en una lista,
puedes usar la clase deque del módulo collections.
Esta estructura permite añadir y eliminar elementos de ambos extremos de manera eficiente.
"""

from collections import deque

# Crear una deque vacía
mi_deque = deque()

# Insertar elementos por la izquierda
mi_deque.appendleft(10)
mi_deque.appendleft(20)
mi_deque.appendleft(30)

# Convertir la deque en una lista (opcional)
mi_lista = list(mi_deque)

# Mostrar el contenido de la deque y la lista
print("Deque:", mi_deque)
print("Lista:", mi_lista)
