# Definición de la función listalimpia que toma un argumento 'arg' y una lista opcional 'result'
def listaLimpia(arg, result=None):
    if result is None:
        result = []  # Si 'result' no se proporciona, se crea una nueva lista vacía
    result.append(arg)  # Se agrega 'arg' a la lista 'result'
    print(result)  # Se imprime la lista después de agregar 'arg'

# Llamada a la función 'listalimpia' con "a" como argumento
listaLimpia("a")

# Llamada a la función 'listalimpia' con "b" como argumento
listaLimpia("b")
