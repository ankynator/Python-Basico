def tabla(num):
    LIMITE = 10
    contador = 1
    num = int(num)

    print('LA TABLA DEL ' + str(num) + ' es:')

    while contador <= LIMITE:

        print('- ' + str(num) + ' x ' + str(contador) + ' = ' + str(contador*num))
        contador = contador + 1


def run():
    numero = input('De que numero quieres saber su tabla de multiplicar? ')
    try:
        numero = int(numero)
        tabla(numero)
    except ValueError:
        print('Asegurate de que sea un NUMERO! ')
        numero = input('De que numero quieres saber su tabla de multiplicar? ')
        tabla(numero)


if __name__ == '__main__':
    run()
