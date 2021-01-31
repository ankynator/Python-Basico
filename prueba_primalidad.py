# PASOS:
# 1. extraer la raiz cuadrada del numero
# 2. obtener los numeros primos menores al resultado de la raiz cuadrada
# 3. dividir el numero que nos dieron entre los primos menores
# 4. Si al menos un resultado tiene residuo entonces el numero no es primo
def primos_menores(prod_raiz):
    contador = 0
    numeros = list(range(1, prod_raiz + 1))
    arr_primos_menores = []

    for i in numeros:
        for j in range(1, i+1):
            if i % j == 0:
                contador += 1
        if contador == 2:
            arr_primos_menores.append(i)
        contador = 0
    return arr_primos_menores


def es_primo(numero):

    contador = 0
    prod_raiz = numero ** 0.5
    prod_raiz = int(prod_raiz)

    arr = primos_menores(prod_raiz)

    for i in arr:
        if(numero % i == 0):
            contador += 1
            break

    if contador != 0 or numero == 1:
        return False
    else:
        return True


def run():
    numero = int(input('Escribe un numero: '))
    if es_primo(numero):
        print('Es primo!')
    else:
        print('No es primo')


if __name__ == '__main__':
    run()
