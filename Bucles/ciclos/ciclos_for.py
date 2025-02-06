#1) Suma de los n primeros números solicite al usuario el numero de elementos a suma 

n= int(input("Ibgrese cuantos elemtos quiere sumar: "))

suma = 0
for i in range(1, n+1):
    suma += i

print("La suma de los elementos", n, "los primeros numero son", suma)

#################################################################################################
# 2) Digite un numero si el numero supera a 10 multiplique los 10 primeros numeros si no sumelos

numero = int(input("Digite un numero: "))

if numero > 10:
    multi = 1
    for i in range(1, 11):
        multi *= i
    resultado = multi

else:
    suma = 0
    for i in range(1, numero + 1):
        suma += i
    resultado = suma
print("el resultado es:", resultado)

#################################################################################################
#3) Escribir un programa que pida el nombre al usuario y lo muestre 10 veces por pantalla 

nombre = input("Dijite su nombre: ")

for i in range(10):
    print(nombre)

#################################################################################################
# 4) Sumar pares desde 0 hasta el numero que indique el usuario

numero = int(input("Ingrese un numero: "))

suma = 0
for i in range(0, numero + 1, 2):
    suma += i

print("La suma de los numero da:", suma, "hasta llegar el numero ingresado que es:", numero)

#################################################################################################
#5) Hacer un programa que imprima la suma de todos los numeros impares desde 1 hasta n y diga cuantos numeros impares hay

numero = int(input("Digite un numero: "))

suma = 0
contador = 0

for i in range(1, numero + 1, 2):
    suma += i 
    contador += 1

print("la suma de los numeros da:", suma, "\nlos impares que hay son:", contador)

#################################################################################################
#6) Hacer un programa que pida dos numeros y muestre todos los numeros que van desde el primero al segundo validar que el primer numero sea menor que el segundo

numero1 = int(input("Digite el primer numero: "))
numero2 = int(input("Digite el segundo número: "))

if numero1 < numero2:
    for i in range(numero1, numero2 + 1):
        print(i)
else:
    print("El primer número debe ser menor que el segundo número.")

#################################################################################################
#7) Algoritmo que pregunte al usuario que tabla de multiplicar quiere ver, debe generar la tabla de multiplicar desde cero hasta 10

numero = int(input("Digite el numero de la tabla de multiplicar que quieres ver: "))

print("tabla de multiplicar", numero,":")
for i in range(11):
    tabla = numero * i
    print(numero, "•", i, "=", tabla)

#################################################################################################
#8) Un maestro de escuela necesita un algoritmo que capture n notas de un estudiante y calcule el promedio

numero = int(input("Ingrese la cantidad de notas a capturar: "))

notas = [] #[] se utiliza para crear una lista vacía
for i in range(numero):
    nota = float(input("Ingrese la nota {}: ".format(i + 1))) #.format() se utiliza para reemplazar los campos de sustitución {}
    notas.append(nota) #para ingresar cada nota para permiter la captura de todas las notas ingresadas

promedio = sum(notas) / numero

print("El promedio es:", promedio)

#################################################################################################
#9) Escribir los numeros del 2 al 10 haciendo aumentos de 2

for numero in range(2, 11, 2): #se puede cambiar el i por otro texto dependiendo lo necesario 
    print(numero)

#################################################################################################
#10) Elabora un algoritmo que pida un numero entero mayor que creo y que escriba sus divisores. validar que el usuario haya ingresado un numero mayor a cero

numero = int(input("Ingrese un número entero mayor que cero: "))

if numero > 0:
    print("Divisores de", numero, ":")
    for i in range(1, numero + 1):
        if numero % i == 0:
            print(i)
else:
    print("El número debe ser mayor que cero.")

#################################################################################################
#11) Elabore un algoritmo que pregunte cuantas temperaturas se van a introducir pida esas temperatura y escriba la temperatura mas alta la mas baja y la temperatura promedio 

cantidadTemperaturas = int(input("Digite la cantidad de temperaturas: "))

temperaturas = []
for i in range(cantidadTemperaturas):
    temperatura = float(input("Digite la temperatura {}: ".format(i + 1)))
    temperaturas.append(temperatura)

temperaturaMaxima = max(temperaturas)
temperaturaMinima = min(temperaturas)
temperaturaPromedio = sum(temperaturas) / cantidadTemperaturas

print("La temperatura mas alta es:", temperaturaMaxima, "\nLa temperatura minima es:", temperaturaMinima, f"\nLa temperatura promedio es: {temperaturaPromedio:.2f}")

#################################################################################################
#12) Elabora un algoritmo que pida las 4 notas de n estudiantes e imprima la nota mas alta, la nota mas baja y el promedio

numero = int(input("Digite la cantidad de estudiantes: "))

notasMasAltas = []
notasMasBajas = []
promedios = []

for i in range(numero):
    notas = []
    for j in range(4):
        nota = float(input("Digite la nota {} del estudiante {}: ".format(j + 1, i + 1)))
        notas.append(nota)
    
    notaMaxima = max(notas)
    notaMinima = min(notas)
    promedio = sum(notas) / 4
    
    notasMasAltas.append(notaMaxima)
    notasMasBajas.append(notaMinima)
    promedios.append(promedio)

notaMasAlta = max(notasMasAltas)
notaMasBaja = min(notasMasBajas)
promedioDeTodos = sum(promedios) / numero

print("La nota más alta es:", notaMasAlta, "\nLa nota más baja es:", notaMasBaja, f"\nEl promedio global es: {promedioDeTodos:.1f}")

