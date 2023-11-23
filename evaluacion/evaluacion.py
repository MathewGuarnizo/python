# Definición de la clase Votante
class Votante:
    def __init__(self, id, nombre):
        # Constructor de la clase Votante.
        self.id = id
        self.nombre = nombre
        self.voto = None  # Almacena el voto del votante

# Definición de la clase Candidato
class Candidato:
    def __init__(self, nombre):
        # Constructor de la clase Candidato.
        self.nombre = nombre
        self.votos = 0  # Contador de votos recibidos por el candidato

# Definición de la clase SistemaVotacion
class SistemaVotacion:
    def __init__(self, candidatos):
        # Constructor de la clase SistemaVotacion.
        self.votantes = []  # Lista de votantes registrados
        self.candidatos = candidatos  # Lista de candidatos disponibles

    def registrarVotante(self, id, nombre):
        # Registra a un nuevo votante en el sistema
        votante = Votante(id, nombre)
        self.votantes.append(votante)
        print(f"Votante {nombre} registrado con éxito.")

    def ingresarSistema(self, id):
        # Permite que un votante registrado ingrese al sistema de votación.
        votante = self.buscarVotantePorId(id)
        if votante:
            print(f"Bienvenido, {votante.nombre}.")
            self.menuVotacion(votante)
        else:
            print("Votante no encontrado.")

    def menuVotacion(self, votante):
        # Despliega el menú de votación para un votante.
        while True:
            print("\n--- Menu de Votacion ---")
            print("1. Votar por Candidato")
            print("2. Votar en Blanco")
            print("3. Volver al Menu Principal")

            opcion = int(input("Ingrese su opcion: "))

            if opcion == 1:
                self.mostrarCandidatos()
                candidato = input("Ingrese el nombre del candidato: ")
                self.votar(votante.id, candidato)
            elif opcion == 2:
                self.votarEnBlanco(votante.id)
            elif opcion == 3:
                break
            else:
                print("Opcion no valida, intentelo de nuevo")

    def votar(self, id, candidato):
        # Registra el voto de un votante por un candidato.
        votante = self.buscarVotantePorId(id)
        if votante and not votante.voto:
            candidatoEncontrado = next((c for c in self.candidatos if c.nombre == candidato), None)
            if candidatoEncontrado:
                candidatoEncontrado.votos += 1
                votante.voto = candidatoEncontrado
                print(f"Su voto fue registrado con exito para {candidato}.")
            else:
                print("Candidato no fue encontrado")
        elif not votante:
            print("Votante nofue  encontrado")
        else:
            print("Este votante ya realizo su voto respectivo")

    def votarEnBlanco(self, id):
        # Registra el voto en blanco de un votante.
        votante = self.buscarVotantePorId(id)
        if votante and not votante.voto:
            print("Voto en blanco se a realizado con exito")
            votante.voto = "Blanco"
        elif not votante:
            print("Votante no se a encontrado")
        else:
            print("Este votante ya reliazo su voto respectivo")


    def mostrarCandidatos(self):
        # este metodo nos ayuda a imprimir la lista de candidatos disponibles para votar
        print("\n--- Candidatos ---")
        for candidato in self.candidatos:
            print(f"{candidato.nombre}")

    def buscarVotantePorId(self, id):
        # Busca al votante por su id
        return next((votante for votante in self.votantes if votante.id == id), None)


# Aqui hacemos la creacion de los respectivos candidatos para votar
candidato1 = Candidato("Adriana Rincon")
candidato2 = Candidato("Miguel Perez")
candidato3 = Candidato("Volibear Herdandez")
candidatos = [candidato1, candidato2, candidato3]

# aqi creamos el sistema de votacion
sistemaVotacion = SistemaVotacion(candidatos)

# Aqui tenemos el menu principal
while True:
    print("\n--- Menu Principal ---")
    print("1. Registrar Votante")
    print("2. Ingresar al Sistema de Votacion")
    print("3. Terminar Votación")
    print("4. Salir")

    opcion = int(input("Ingrese su opción: "))

    if opcion == 1:
        id = int(input("Ingrese el ID del votante: "))
        nombre = input("Ingrese el nombre del votante: ")
        sistemaVotacion.registrarVotante(id, nombre)
    elif opcion == 2:
        id = int(input("Ingrese el ID del votante: "))
        sistemaVotacion.ingresarSistema(id)
    elif opcion == 3:
        sistemaVotacion.terminarVotacion()
        break
    elif opcion == 4:
        break
    else:
        print("Opcion no valida, intentelo de nuevo")
