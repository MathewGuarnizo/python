def unir_tuplas(tupla1, tupla2): #funcion unir
    tupla_unida = tupla1 + tupla2
    return tupla_unida

tupla1 = (5, 6, 7) #une las dos tuplas 
tupla2 = (1, 2, 3)
resultado = unir_tuplas(tupla1, tupla2)
print(resultado)