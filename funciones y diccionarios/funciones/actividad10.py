# Definición de una función lambda llamada operadorand que realiza la operación AND bit a bit entre X e Y
operadorand = lambda x, y: x & y

# Bucle anidado para iterar a través de todas las combinaciones de valores 0 y 1 para i y j
for i in range(2):
    for j in range(2):
        # Imprime la operación AND entre i y j
        print(f"{i} & {j} = {operadorand(i, j)}")
