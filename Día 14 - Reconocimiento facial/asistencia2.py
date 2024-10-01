import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Crear base de datos de empleados
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

print(nombres_empleados)

# Codificar imágenes
def codificar(imagenes):
    lista_codificada = []
    for imagen_p in imagenes:
        imagen_p = cv2.cvtColor(imagen_p, cv2.COLOR_BGR2RGB)
        codificado = fr.face_encodings(imagen_p)[0]
        lista_codificada.append(codificado)
    return lista_codificada

# Registrar los ingresos
def registrar_ingresos(persona):
    f = open('registro.csv', 'r+')
    lista_datos = f.readlines()
    nombres_registro = []
    for linea in lista_datos:
        ingreso = linea.split(',')
        nombres_registro.append(ingreso[0])

    if persona not in nombres_registro:
        ahora = datetime.now()
        string_ahora = ahora.strftime('%H:%M:%S')
        f.writelines(f'\n{persona}, {string_ahora}')
    f.close()

lista_empleados_codificada = codificar(mis_imagenes)

# Iniciar captura de cámara
captura = cv2.VideoCapture(0)

if not captura.isOpened():
    print("Error al acceder a la cámara")
    exit()

# Bucle para capturar continuamente
while True:
    exito, imagen = captura.read()

    if not exito:
        print("No se ha podido tomar la captura")
        break

    # Reconocer cara en captura
    cara_captura = fr.face_locations(imagen)
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)

    # Buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)

        indice_coincidencia = numpy.argmin(distancias)

        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguno de nuestros empleados")
        else:
            nombre = nombres_empleados[indice_coincidencia]
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)

            registrar_ingresos(nombre)

    # Mostrar la imagen obtenida
    cv2.imshow('Imagen web', imagen)

    # Presionar 'q' para salir del bucle
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Liberar la cámara y cerrar ventanas
captura.release()
cv2.destroyAllWindows()
