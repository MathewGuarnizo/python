# Definición de una función lambda llamada numero_palabras que toma una cadena t como argumento
# La función lambda divide la cadena en palabras y cuenta la cantidad de palabras
numero_palabras = lambda t: len(t.strip().split())

# Llamada a la función lambda con una cadena de texto como argumento
# La cadena se divide en palabras y se cuenta la cantidad de palabras
resultado = numero_palabras("hola, esto es una prueba con lambda")

# Imprimir el resultado
print(resultado)