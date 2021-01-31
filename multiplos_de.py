def run():
    multiplo = int(input('De que numero quieres saber sus multiplos: '))
    cifras = int(input('Ingresa la cantidad de cifra maxima: '))

    LIMITE = (10 ** cifras) - 1
    contador = 0

    while contador < 100000:
        contador = contador + 1
        if contador % multiplo != 0:
            continue
        if contador > LIMITE:
            break
        print(contador)

    print(LIMITE)


if __name__ == '__main__':
    run()
