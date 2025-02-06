#Excepción de índice fuera de rango (IndexError)
def obtener_elemento(lista, indice): 
    try:
        elemento = lista[indice]
        print("El elemento es:", elemento)
    except IndexError:
        print("Error: El índice está fuera del rango válido.")

lista = [1, 2, 3, 4, 5]
obtener_elemento(lista, int(input("digite un numero: ")))