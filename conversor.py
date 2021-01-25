dolares = input("¿Cuántos dolares tienes? ")
dolares = float(dolares)
valor_sol = 0.28

soles = dolares / valor_sol
soles = round(soles, 2)
soles = str(soles)
print("Tienes $" + soles + " dólares")
