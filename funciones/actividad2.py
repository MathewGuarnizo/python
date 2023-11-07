# Definición de una función llamada 'lista' que toma dos argumentos, dia y semana con un valor predeterminado de una lista vacía.
def lista(dia, semana=[]):
    
    # Agrega el valor dia a la lista semana.
    semana.append(dia)
    
    # Imprime la lista semana después de agregar dia.
    print(semana)

# Llama a la función lista con un valor para dia y una lista inicial proporcionada como argumentos.
lista("Domingo", ["Lunes", "Martes", "Miercoles", "Jueves", "Sabado"])