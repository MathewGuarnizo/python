#Consulte un ejemplo donde se declare una clase con atributos y métodos.

# Definición de la clase Empleado
class Empleado:
    # Constructor de la clase Empleado con tres parámetros: nombre, apellido y salario
    def __init__(self, nombre, apellido, salario):
        # Asignación de los valores recibidos a los atributos del objeto
        self.nombre = nombre
        self.apellido = apellido
        self.salario = salario

    # Método para obtener el nombre completo del empleado
    def obtenerNombreCompleto(self):
        return f"{self.nombre} {self.apellido}"

    # Método para obtener el salario del empleado
    def obtenerSalario(self):
        return self.salario

    # Método para incrementar el salario del empleado en una cantidad dada
    def incrementarSalario(self, incremento):
        self.salario += incremento  # Incremento del salario
        return self.salario  # Devuelve el salario actualizado

# Creación de una instancia de la clase Empleado con valores específicos
empleado1 = Empleado("Kevin", "Pérez", 3000)

# Llamada al método obtener_nombre_completo para obtener el nombre completo del empleado
nombreCompleto = empleado1.obtenerNombreCompleto()
print(f"Nombre completo: {nombreCompleto}")  # Imprime el nombre completo del empleado

# Llamada al método obtener_salario para obtener el salario del empleado
salario = empleado1.obtenerSalario()
print(f"Salario: {salario}")  # Imprime el salario del empleado

# Llamada al método incrementar_salario para aumentar el salario del empleado en 500 unidades
nuevoSalario = empleado1.incrementarSalario(500)
print(f"Nuevo salario: {nuevoSalario}")  # Imprime el nuevo salario del empleado

print("-------------------------------------------------------------------------------------------------------")

# #Consulte un ejemplo donde se implemente la herencia.

# Definición de la clase Animal
class Animal:
    def __init__(self, especie, edad):  # Método constructor de la clase Animal
        self.especie = especie  # Asigna el parámetro especie al atributo especie de la instancia
        self.edad = edad  # Asigna el parámetro edad al atributo edad de la instancia

    def hablar(self):  # Método hablar de la clase Animal
        print("Soy un", self.especie)  # Imprime un mensaje indicando la especie del animal

# Definición de la clase Perro que hereda de la clase Animal
class Perro(Animal):
    def __init__(self, nombre, edad):  # Método constructor de la clase Perro
        super().__init__("Perro", edad)  # Llama al constructor de la clase Animal con "Perro" como especie
        self.nombre = nombre  # Asigna el parámetro nombre al atributo nombre de la instancia de Perro

    def hablar(self):  # Método hablar de la clase Perro
        print("Guau, guau. Soy", self.nombre)  # Imprime el ladrido del perro junto con su nombre

# Definición de la clase Gato que hereda de la clase Animal
class Gato(Animal):
    def __init__(self, nombre, edad):  # Método constructor de la clase Gato
        super().__init__("Gato", edad)  # Llama al constructor de la clase Animal con "Gato" como especie
        self.nombre = nombre  # Asigna el parámetro nombre al atributo nombre de la instancia de Gato

    def hablar(self):  # Método hablar de la clase Gato
        print("Miau, miau. Soy", self.nombre)  # Imprime el maullido del gato junto con su nombre

# Creación de una instancia de Perro con nombre "Max" y edad 5
perro = Perro("Max", 5)
# Creación de una instancia de Gato con nombre "Felix" y edad 3
gato = Gato("Felix", 3)

# Llamada al método hablar de la instancia perro (imprime el ladrido del perro)
perro.hablar()
# Llamada al método hablar de la instancia gato (imprime el maullido del gato)
gato.hablar()


print("-------------------------------------------------------------------------------------------------------")

#Consulte un ejemplo donde se implemente el polimorfismo

# Definición de la clase Empleado
class Empleado:
    def __init__(self, nombre, cargo, salarioBase):
        self.nombre = nombre
        self.cargo = cargo
        self.salarioBase = salarioBase

    def calcularSalario(self):
        pass

class Programador(Empleado):
    def calcularSalario(self):
        return self.salarioBase * 1.1

class Administrativo(Empleado):
    def calcularSalario(self):
        return self.salarioBase * 1.05

class Comercial(Empleado):
    def calcularSalario(self):
        return self.salarioBase * 1.15
    

empleados = [
    Programador("Juan", "Programador", 3000),
    Administrativo("Maria", "Administrativo", 2500),
    Comercial("Pedro", "Comercial", 4000)
]

for empleado in empleados:
    print(f"El salario de {empleado.nombre} es {empleado.calcularSalario()}")
