#Declaramos la varaible 
calificaciones = {
'nombre': 'Mathew',
'notafinal': 4.5
}

#Agregamos mas nombre y calificaciones
calificaciones = {
'Mathew': 4.5,
'Kevin':3.0,
'Valentina':4.0,
'Laura':2.9

}

# agregamos estudiantes nuevos
calificaciones.update({"Maria": 3.4, "Raul": 4.9})

# Iterar a través del diccionario calificaciones
for i, j in calificaciones.items():
    # En cada iteración, i contiene la clave (nombre del estudiante) y j contiene el valor (calificación)

    #imprime el nombre del estudiante y la nota
    print(i, j)