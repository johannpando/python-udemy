lista = ['a', 'b', 'c', 'd']
print(type(lista))
mis_tuples = list(enumerate(lista))
print((type(mis_tuples)))

for t in mis_tuples:
    print(t, type(t))


for i, v in mis_tuples:
    print(i, v)

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

mi_tuple = list(enumerate(lista_nombres))

for indice, nombre in mi_tuple:
    print(f'{nombre} se encuentra en el índice {indice}')

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]

mi_tuple = list(enumerate(lista_nombres))

for i, v in mi_tuple:
    if v.startswith('M'):
        print(v)