def obtenerValorMaximo(diccionario):    #Obtiene el valor máximo de un diccionario.

    valores = list(diccionario.values())
    return max(valores)

diccionario2 = {'a': 10, 'b': 5, 'c': 8} #argumento
valor_maximo = obtenerValorMaximo(diccionario2)
print("Valor máximo:", valor_maximo)
