# Definición de la función compra que calcula el costo total de una compra
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad  # Calcula el costo total
    )

# Llamada a la función compra con los argumentos: marca=AMD, cantidad=3, valor=2500000
# La función devuelve un diccionario con información sobre la compra
compraRealizada = compra("AMD", 3, 2500000)

# Imprime la información de la compra
print(f'Lo comprado fue: {compraRealizada}')
