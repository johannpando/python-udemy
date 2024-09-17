import numeros


def preguntar_usuario():
    print("Bienvenido a la farmacia Python")
    while True:
        print("[P] - Perfumería\n[F] - Farmacia\n[C] - Cosmética")
        try:
            tipo = input("Elija la categoría: ").upper()
            ["P", "F", "C"].index(tipo)
        except ValueError:
            print("Opción no válida")
        else:
            break
    numeros.decorador(tipo)


# Iniciar programa
def inicio():
    while True:
        preguntar_usuario()  # Llama a la función al principio del ciclo
        while True:
            try:
                otro_turno = input("¿Quiere sacar otro turno? [S] [N]: ").upper()
                # Verificamos si la opción ingresada es válida
                ["S", "N"].index(otro_turno)
            except ValueError:
                print("Opción no válida")
                continue  # Si hay un error, vuelve a preguntar
            else:
                if otro_turno == "N":
                    print("Gracias por su visita")
                    return  # Salimos de la función
                else:
                    break  # Salimos del bucle interno para continuar


inicio()
