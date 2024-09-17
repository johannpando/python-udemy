import datetime

mi_hora = datetime.time(17, 23)
print(mi_hora)

mi_fecha = datetime.date(2020, 10, 6)
print(mi_fecha)
print(mi_fecha.ctime())

# hoy


from datetime import date, time

nacimiento = date(1980, 12, 9)
fallecimiento = date(2024, 9, 13)

vida = fallecimiento - nacimiento

print(f"Ha vivido {vida.days} días")

hoy = date.today()
print(hoy)


from datetime import datetime

# Obtener la hora actual
hora_actual = datetime.now()

# Extraer los minutos
minutos = hora_actual.minute

# Mostrar el resultado
print(f"Los minutos actuales son: {minutos}")

