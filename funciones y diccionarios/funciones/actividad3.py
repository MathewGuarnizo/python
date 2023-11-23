# Definición de una función llamada 'actividad' que toma dos argumentos, 'x' e 'y'
def actividad(x, y):
    
    # Calcula el resultado de la operación: x * 2 + y * 2
    resultado = x * 2 + y * 2
    
    # Imprime el resultado con un mensaje descriptivo
    print(f"El resultado de la operación de {x} x 2 + {y} x 2 es: {resultado}")

# Solicita al usuario que ingrese el valor de x y el valor de y, y llama a la función 'actividad'
x = int(input("Inserte el valor de X: "))
y = int(input("Inserte el valor de Y: "))

#Llamamos la función
actividad(x, y)