def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for k, v in kwargs.items():
        print(f"{k}: {v}")


mi_diccionario = {"color_ojos": "azules", "color_cabello": "negro"}
describir_persona("Juana", **mi_diccionario)
