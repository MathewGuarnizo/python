# Listas de nombres y edades
nombres = ['Maria', 'Sebastian', 'Ana']
edades = ['18', '25', '30']

# Usar la función zip para combinar las listas nombres y edades
# Luego, iterar a través de los pares combinados y mostrar el nombre y la edad
for n, e in zip(nombres, edades):

    # En cada iteración, n contiene un nombre y e contiene una edad
    # Utilizar el método format para crear una cadena con el nombre y la edad
    print('Tú nombre es {0} y tu edad {1}.'.format(n, e))