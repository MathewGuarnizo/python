# Definición de la función 'raiz' que calcula la raíz cuadrada de un valor
def raiz(value):
    return value ** (1/2)

# Llamada a la función 'raiz' con el valor 4 y se imprime el resultado
print(f'La raiz cuadrada es: {raiz(4)}')

# Definición de la función 'validarsiexiste' que verifica si un objeto es verdadero o falso
def validarSiExiste(obj):
    if obj:
        print(f"{obj} is True")
    else:
        print(f"{obj} is False")

# Llamada a la función 'validarsiexiste' con el valor 1 y se imprime si es True
validarSiExiste(1)