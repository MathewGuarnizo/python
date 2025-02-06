def encontrar_maximo(tupla): #funcion encontrar maximo
    maximo = max(tupla)
    return maximo

mi_tupla = (int(input("digite un numero: ")),int(input("digite un numero: ")),int(input("digite un numero: ")),int(input("digite un numero: ")),int(input("digite un numero: "))) #de aqui ingresa el numero mas alto
resultado = encontrar_maximo(mi_tupla)
print(resultado)