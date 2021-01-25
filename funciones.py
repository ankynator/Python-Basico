# def imprimir_mensaje():
#     print('Mensaje especial: ')
#     print('Estoy aprendiendo a usar funciones! ')

# imprimir_mensaje()
# imprimir_mensaje()
# imprimir_mensaje()

def saludar(op):
    # op = str(op)
    print('Hola 😃')
    print('Como estas')
    print('Elegiste la opcion ' + op)
    print('Adios')


opcion = input('Elige una opcion (1, 2, 3): ')

if opcion == '1':
    saludar(opcion)
elif opcion == '2':
    saludar(opcion)
elif opcion == '3':
    saludar(opcion)
else:
    print('Escoge una opcion valida por favor 😃')
