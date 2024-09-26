import speech_recognition as sr


# Escucha el micrófono y transforma audio a texto
def transformar_audio_a_texto():
    # Almacena recognizer en una variable
    r = sr.Recognizer()

    # Configura el micrófono
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("Se está grabando...")

        # Guardar el audio
        audio = r.listen(origen)

        try:
            # Reconocer el audio usando Google
            pedido = r.recognize_google(audio, language="es-ES")
            print(f"He escuchado: {pedido}")
            return pedido
        except sr.UnknownValueError:
            print("Lo siento, no entendí lo que dijiste.")
        except sr.RequestError as e:
            print(f"No se puede conectar al servicio de Google; {e}")


# Llamar a la función
# transformar_audio_a_texto()
