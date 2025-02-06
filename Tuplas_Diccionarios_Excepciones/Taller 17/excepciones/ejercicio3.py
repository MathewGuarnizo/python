#Excepción de tipo de dato incorrecto (TypeError)
def sumar(a, b):
    try:
        resultado = a + b
        print("El resultado de la suma es:", resultado)
    except TypeError:
        print("Error: Se esperaban operandos numéricos.")

sumar(int(input("Digite un numero: ")), int(input("Digite un numero o letra: ")))