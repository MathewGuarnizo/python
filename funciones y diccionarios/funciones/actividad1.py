# Definición de la función saludar que imprime un saludo
def saludar():
    print("saludo")

# Definición de la función retornarnumero que devuelve el número 1
def retornarNumero():
    return 1

# Llamada a la función saludar() que imprime un saludo
saludar()

# Llamada a la función retornarnumero()
retornarNumero()

# Comprobación de si la función retornarnumero() devuelve 1 y se imprime el resultado
if retornarNumero() == 1:
    print("devolvió un uno")
else:
    print("No devolvió un uno")
