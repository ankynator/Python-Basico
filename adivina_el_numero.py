import random


def run():
    numero_aleatorio = random.randint(1, 100)
    numero_elegido = int(input('Elige un numero del 1 al 100: '))
    frase = ''
    vidas = 5

    while numero_elegido != numero_aleatorio and vidas > 0:
        if numero_elegido < numero_aleatorio:
            frase = 'mas grande: '
        else:
            frase = 'mas pequeño: '

        numero_elegido = int(input('Busca un numero ' + frase))
        vidas -= 1

    if vidas == 0:
        print('¡Ganaste!🥇 adivinaste -> ' + str(numero_aleatorio))
    else:
        print('Se te acabaron las vidas 💔 el numero era ' + str(numero_aleatorio))


if __name__ == '__main__':
    run()
