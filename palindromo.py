def palindromo(frase):
    frase = frase.replace(' ', '')
    frase = frase.lower()
    frase_p = frase[::-1]

    if frase == frase_p:
        return True
    else:
        return False


def run():
    frase = input('Escribe una palabra: ')
    es_palindromo = palindromo(frase)
    if es_palindromo == True:
        print('Es palindromo')
    else:
        print('No es palindromo')


if __name__ == '__main__':
    run()
