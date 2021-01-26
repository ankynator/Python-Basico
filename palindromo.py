def es_palindromo(frase):
    frase = frase.replace(' ', '').lower()
    frase_p = frase[::-1]

    if frase == frase_p:
        print(frase + ' Es palindromo!')
    else:
        print(frase + ' No es palindromo!')


f = input('Ingresa una palabra: ')
es_palindromo(f)
