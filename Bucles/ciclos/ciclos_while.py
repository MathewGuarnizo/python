#1) Digite un numero si el numero supera a 10 multiplica los 10 primeros numeros sino sumelos 

numero = int(input("Digite un número: "))

resultado = 1  # Inicializamos el resultado en 1 para la multiplicación
contador = 1

if numero > 10:
    while contador <= 10:
        resultado *= contador
        contador += 1
else:
    while contador <= numero:
        resultado += contador
        contador += 1

print("El resultado es:", resultado)

#########################################################################################################################################################################
#2) Sumar pares desde 0 hasta el numero que indique el usuario 

numero = int(input("Digite un numero: "))

suma = 0
contador = 0

while contador <= numero:
    if contador % 2 == 0:
        suma += contador 
    contador += 1

print("La suma de los numero da:", suma, "hasta llegar el numero ingresado que es:", numero)

#################################################################################################
#3) Hacer un programa  que imprima la suma de todos los números impares desde 1 hasta n, y diga cuantos números impares hay

numero = int(input("Digite un número: "))

sumaImpares = 0
cantidadImpares = 0
num = 1

while num <= numero:
    if num % 2 != 0:
        sumaImpares += num
        cantidadImpares += 1
    num += 1     
print("La suma de los números impares es:", sumaImpares, "\nLa cantidad de números impares es:", cantidadImpares)

#################################################################################################
#4) Hacer un programa que pida dos numeros y muestre  todos los numeros que van desde el primero al segundo validar que el primer numero sea menor que el segundo

primerNumero = int(input("Ingrese el primer número: "))
segundoNumero = int(input("Ingrese el segundo número: "))

while primerNumero >= segundoNumero:
    print("El primer número debe ser menor que el segundo. Intente nuevamente.")
    primerNumero = int(input("Ingrese el primer número: "))
    segundoNumero = int(input("Ingrese el segundo número: "))

numeroActual = primerNumero

print("Los números desde", primerNumero, "hasta", segundoNumero, "son:")

while numeroActual <= segundoNumero:
    print(numeroActual)
    numeroActual += 1

#################################################################################################
#5) Crear un programa que permita al usuario ingresar los valores totales de n factura (se desconoce la cantidad de datos que cargara, la cual puede cambiar en cada ejecucion), cortando el ingreso de datos cuando el usuario ingrese el monto 0. Al finalizar, informar el total a pagar teniendo que cuenta que, si las ventas superan el total de $1000, se le debe aplicar un 10% de descuento.

totalPagar = 0

while True:
    monto = float(input("Ingrese el monto de la factura (0 para finalizar): "))
    if monto == 0:
        break
    totalPagar += monto

if totalPagar > 1000:
    descuento = totalPagar * 0.1
    totalPagar -= descuento

print("El total a pagar es:", totalPagar)

#################################################################################################
#6) Un maestro de escuela necesita un algoritmo que capturen n notas de un estudiante y calcule el promedio

numero = int(input("Digite la cantidad de notas: "))
sumaNotas = 0
contador = 0

while contador < numero:
    nota = float(input("Digite la nota: "))
    sumaNotas += nota
    contador += 1

promedio = sumaNotas / numero
print(f"El promedio es: {promedio:.1f}")

#################################################################################################
#7) Leer números enteros del teclado, hasta que el usuario ingrese el 0. Finalmente, mostrar la sumatoria de todos los numeros ingresados

suma = 0
numero = int(input("Ingrese un número entero (0 para finalizar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número entero (0 para finalizar): "))

print("La sumatoria de los números ingresados es:", suma)

#################################################################################################
#8) Elabora un algoritmo que permita ingresar n numero entero mayor que cero y escriba sus divisores. validar que el usuario haya ingresado un numero mayor a cero
numero = int(input("Digite un número: "))

while numero <= 0:
    print("El número debe ser mayor que cero. Intente nuevamente.")
    numero = int(input("Digite un número entero mayor que cero: "))

divisores = []
i = 1

while i <= numero:
    if numero % i == 0:
        divisores.append(i)
    i += 1

print("Los divisores de", numero, "son:", divisores)

#################################################################################################
#9) Elabore un algoritmo que permita ingresar n numero de temperaturas y escriba la temperatura mas alta, las mas baja y la temperatura promedio

numero = int(input("Ingrese la cantidad de temperaturas: "))

temperaturaMasAlta = float('-inf')
temperaturaMasBaja = float('inf')
sumaTemperaturas = 0
contador = 0

while contador < numero:
    temperatura = float(input("Ingrese la temperatura: "))
    if temperatura > temperaturaMasAlta:
        temperaturaMasAlta = temperatura
    if temperatura < temperaturaMasBaja:
        temperaturaMasBaja = temperatura
    sumaTemperaturas += temperatura
    contador += 1

temperaturaPromedio = sumaTemperaturas / numero

print("La temperatura más alta es:", temperaturaMasAlta, "\nLa temperatura más baja es:", temperaturaMasBaja, f"\nLa temperatura promedio es: {temperaturaPromedio:.1f}")

#################################################################################################
#10) Elabora un algoritmo que pida las 3 notas de n estuidantes e imprima la nota mas alta, la mas baja y el promedio

cantidad = int(input("Digite la cantidad de estudiantes: "))

contador = 1

while contador <= cantidad:
    print(f"\nDigite las 3 notas del estudiante {contador}:")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    notaMasAlta = max(nota1, nota2, nota3)
    notaMasBaja = min(nota1, nota2, nota3)
    promedio = (nota1 + nota2 + nota3) / 3

    print("\nResultados para el estudiante", contador, "\nNota más alta:", notaMasAlta, "\nNota más baja:", notaMasBaja, f"\nPromedio: {promedio:.1f}")

    contador += 1
