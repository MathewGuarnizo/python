
# Definición de la función compra que calcula el costo total de una compra.
# El argumento valor tiene un valor predeterminado de 2,500,000.
def compra(marca, cantidad, valor=2500000):
    # Crea un diccionario con información sobre la compra, incluyendo la marca, cantidad y valor total.
    return dict(
        marca=marca,
        cantidad=cantidad,
        valor=valor * cantidad  # Calcula el costo total
    )

# Imprimir la información de la compra.
print(f' lo comprado fue:{compra("AMD",3)}')



