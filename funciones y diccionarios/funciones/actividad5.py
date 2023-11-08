# Definición de la función compra que calcula el costo total de una compra
def compra(marca, cantidad, valor):
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad  # Calcula el costo total
    )

# Llamada a la función compra con argumentos especificados por nombre
# Esto mejora la claridad y legibilidad del código
compraRealizada = compra(marca="AMD", cantidad=3, valor=2500000)

# Imprime la información de la compra
print(f'Lo comprado fue: {compraRealizada}')