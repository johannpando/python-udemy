import datetime
import pyttsx3
import webbrowser
from audio_a_texto import transformar_audio_a_texto
import wikipedia
import pywhatkit
import pyjokes


def hablar(mensaje):
    # Iniciar
    engine = pyttsx3.init()

    # pronunciar el mensje
    engine.say(mensaje)
    engine.runAndWait()


def saludo_inicial():
    hora = datetime.datetime.now()
    if hora.hour < 6 or hora.hour > 20:
        momento = "Buenas noches"
    elif 6 <= hora.hour < 13:
        momento = "Buen día"
    else:
        momento = "Buenas tardes"

    hablar(f"{momento}, soy tu asistente personal. ¿En qué te puedo ayudar?")


def iniciar_conversacion():
    saludo_inicial()

    comenzar = True

    while comenzar:
        # Activar el micrófono y guardar el pedido en un string
        solicitud = transformar_audio_a_texto().lower()

        if 'abrir youtube' in solicitud:
            hablar("Abriendo youtube")
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in solicitud:
            hablar("Abriendo navegador")
            webbrowser.open('https://www.google.com')
            continue
        elif 'busca en wikipedia' in solicitud:
            hablar('Buscando en Wikipedia')
            solicitud = solicitud.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(solicitud, sentences=1)
            hablar("El resultado de tu búsqueda es el siguiente")
            hablar(resultado)
            continue
        elif 'busca en internet' in solicitud:
            hablar("Estoy en ello")
            solicitud = solicitud.replace('busca en internet', '')
            pywhatkit.search(solicitud)
            hablar("Esto es lo que he encontrado")
            continue
        elif 'cuenta un chiste' in solicitud:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'terminar la conversación' in solicitud:
            hablar('Adiós, puedes volver a comunicarte conmigo cuando quieras')
            break


iniciar_conversacion()
