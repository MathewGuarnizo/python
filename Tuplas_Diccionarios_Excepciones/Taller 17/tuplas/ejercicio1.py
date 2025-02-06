def sumar_tupla(tupla): #funcion sumar tupla que toma una tupla como argumento
    suma = sum(tupla)
    return suma

mi_tupla = (int(input("digite un numero: ")),int(input("digite un numero: ")),int(input("digite un numero: ")),int(input("digite un numero: ")),int(input("digite un numero: ")))  #argumento
resultado = sumar_tupla(mi_tupla)
print(resultado) 
