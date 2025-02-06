def fusionarDiccionarios(diccionario1, diccionario2):   #Fusiona dos diccionarios en uno nuevo.

    diccionario_fusionado = {}
    diccionario_fusionado.update(diccionario1)
    diccionario_fusionado.update(diccionario2)
    return diccionario_fusionado

diccionario3 = {'a': 10, 'b': 11,'c': 12, 'd': 13}
diccionario4 = {'e': 14, 'f': 15,'h': 16, 'j': 17}
diccionario_fusionado = fusionarDiccionarios(diccionario3, diccionario4)
print("Diccionario fusionado:", diccionario_fusionado)