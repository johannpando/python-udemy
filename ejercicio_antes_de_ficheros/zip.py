capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

lista = list(zip(capitales, paises))

for c, p in lista:
    print(f"La capital de {p} es {c}")

