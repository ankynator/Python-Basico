objetos = [1, 3.5, True, 'vander']
objetos2 = ['Zhaida', True, 3]

# concatenar dos o mas listas
objetos_juntados = objetos + objetos2
print(objetos_juntados)

# multiplicar listas -> repite la misma lista
mul = objetos * 2
print(mul)

# Añadir elementos a una lista

print(objetos)
objetos.append('Idme')
print(objetos)

# Eliminar el ultimo elemento y un elemento dado un indice

obj_ultimo_elemento = objetos.pop()
print(obj_ultimo_elemento, objetos)

obj_indice = objetos.pop(2)
print(obj_indice, objetos)

# Ordenar un lista de mayor a menor, NO SE MODIFICA LA LISTA INICIAL

numeros_inicial = [2, 4, 3, 1, 5, 7, 6, 9, 8]
ordenados_1 = sorted(numeros_inicial)

print(ordenados_1)

# Ordenar la lista modificando la lista original

numeros_inicial.sort()
print(numeros_inicial)

# Eliminar elementos dando el valor del elemento

numeros = [1, 2, 23, 3, 4, 5]
print(numeros)
numeros.remove(23)
print(numeros)

# Tamaño de la lista

print(len(numeros))
