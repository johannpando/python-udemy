import bs4
import requests

"""
La página toscrape es gratuita y permite realizar web scrpaing sin problemas
El ejercicio se basa en recorrer varias páginas y almacenar los títulos de libros con más de 5 estrellas
"""

url_base = 'https://books.toscrape.com/catalogue/page-{}.html'
# La página irá cambiando dinámicante
print(url_base.format('3'))
# Imprime https://books.toscrape.com/catalogue/page-3.html

# Solo queremos los libros de 5 estrellas, para ello tenemos que inspeccionar el objeto que pinta las estrellas
resultado = requests.get(url_base.format('1'))
estructura = bs4.BeautifulSoup(resultado.text, 'lxml')
# Todos los libros están contenidos en una clase, para ello usamos el punto
print(estructura.select('.product_pod'))
libros = estructura.select('.product_pod')
ejemplo_titulo = libros[0].select('a')[1]['title']
print(ejemplo_titulo)
print('*' * 25)

lista_titulos = []
# Interamos las páginas
for pagina in range(1, 10):
    url_pagina = url_base.format(pagina)
    # print(url_pagina)
    resultado = requests.get(url_pagina)
    estructura = bs4.BeautifulSoup(resultado.text, 'lxml')
    libros = estructura.select('.product_pod')
    # print(len(libros))

    for libro in libros:
        # Verificar las estrellas
        # Usamos un punto si la clase tiene espacio
        if len(libro.select('.star-rating.Four')) != 0 or len(libro.select('.star-rating.Five')) != 0:
            # print('cumple condición')
            # Guardamos el titulo
            titulo_libro = libro.select('a')[1]['title']
            # print(titulo_libro)
            # Agregamos el libro a la lista
            lista_titulos.append(titulo_libro)

print('*' * 25)

for titulo in lista_titulos:
    print(titulo)



