def convertir(v_dolar, p):
    valor_dolar = v_dolar
    dolares = p / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dólares")


def preguntar(tipo_peso):
    pesos = input("¿Cuántos pesos " + tipo_peso + " tienes? ")
    pesos = float(pesos)
    return pesos


menu = """
Bienvenido al conversor de monedas 💰
1 - Pesos colombianos
2 - Pesos argentinos
3 - Pesos mexicanos

Elige una opcion: """

pesos = 0

opcion = input(menu)

if opcion == '1':
    pesos_colombianos = preguntar("colombianos")
    convertir(3875, pesos_colombianos)
elif opcion == '2':
    pesos_argentinos = preguntar("argentinos")
    convertir(65, pesos_argentinos)
elif opcion == '3':
    pesos_mexicanos = preguntar("mexicanos")
    convertir(24, pesos_mexicanos)
else:
    print('Por favor introduce una opcion valida 💸')
