#Excepción de división entre cero (ZeroDivisionError)
def dividir(a, b): 
    try:
        resultado = a / b
        print("El resultado de la división es:", resultado)
    except ZeroDivisionError:
        print("Error: No se puede dividir entre cero.")

dividir(int(input("Digite el dividendo: ")), int(input("Digite el divisor: ")))