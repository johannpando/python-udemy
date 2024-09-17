def generador_numeros():
    num = 4
    while num > 1:
        num = num - 1
        print(f"Te quedan {num} vidas")
        yield num
    print("Game Over")


perder_vida = generador_numeros()

# Consumir el generador para perder vidas
for _ in perder_vida:
    pass
