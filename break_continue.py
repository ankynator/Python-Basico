def run():
    # for contador in range(1000):
    #     if contador % 2 != 0:
    #         continue
    #     print(contador)

    # for i in range(10000):
    #     print(i)
    #     if i == 5841:
    #         break

    texto = input('Escribe un texto: ')

    for letra in texto:
        if letra == 'o':
            break
        print(letra)


if __name__ == '__main__':
    run()


# --continue-- deja de ejecutar las lineas de abajo
# y se pasa a la siguiente pasada del ciclo -> El ciclo se sigue ejecutando

# --break-- rompe todo y ya no ejecuta mas el ciclo -> El ciclo ya no se ejecuta
