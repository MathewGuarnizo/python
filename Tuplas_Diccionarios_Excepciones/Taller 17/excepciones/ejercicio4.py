#Excepción de archivo no encontrado (FileNotFoundError)
def leer_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo, 'r')
        contenido = archivo.read()
        print("Contenido del archivo:", contenido)
        archivo.close()
    except FileNotFoundError:
        print("Error: El archivo no fue encontrado.")

leer_archivo("archivo.txt")