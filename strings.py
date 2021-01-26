nombre = 'vander '

n_upper = nombre.upper()
print('upper(): ' + n_upper)

n_capitalize = nombre.capitalize()
print('capitalize(): ' + n_capitalize)

n_lower = nombre.lower()
print('lower(): ' + n_lower)

n_replace = nombre.replace('a', 'e')
print('replace(\'a\', \'e\'): ' + n_replace)

n_strip = nombre.strip()
print('strip(): ' + n_strip)

letra = nombre[6]
print('nombre[6]: ' + letra +
      '<- es el espacio en blanco que borramos con strip')

length = str(len(nombre))
print('longitud de \'nombre\': ' + length)
