import bs4
import requests

resultado = requests.get('https://escueladirecta-blog.blogspot.com/2021/09/cohesion-pilares-de-la-programacion.html')
print(type(resultado))  # Imprime <class 'requests.models.Response'>
print(resultado.text)  # Todo el contenido de la web en texto

estructura = bs4.BeautifulSoup(resultado.text, 'lxml')
print(type(estructura))  # Imprime <class 'bs4.BeautifulSoup'>
print(estructura.select('title'))  # Devuelve una lista:
# [<title>Cohesión - Pilares de la Programación Orientada a Objetos en Python</title>]
# Si solo quiero el texto:
print(estructura.select('title')[0].text)
print(estructura.select('p')[0].getText())


# Descargando imagenes
url = requests.get('https://escueladirecta.com/courses')
estructura = bs4.BeautifulSoup(url.text, 'lxml')
imagenes = estructura.select('img')

for i in imagenes:
    print(i)

solo_clases = estructura.select('.course-box-image')

print('*' * 25)
print(len(solo_clases))
for i in solo_clases:
    print(type(i))  # Imprime <class 'bs4.element.Tag'>
    print(i['src'])

print('*' * 25)
# Descargar imagen
una_url = estructura.select('.course-box-image')[0]['src']
imagen = requests.get(una_url)
print(imagen)  # Imprime <Response [200]>
print(imagen.content)  # Imprime un binario

# Crea una imagen
file_imagen = open('mi_imagen.jpg', 'wb')
file_imagen.write(imagen.content)
file_imagen.close()