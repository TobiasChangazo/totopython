# Microdesafío: clase Automovil
class Auto():
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

    def __str__(self):
        return "Marca: " + self.marca + ", Modelo: " + self.modelo

automovil_1 = Auto("Toyota", "Hilux")
print(automovil_1)

# Ejemplo de clase para mostrar algunas cosas más que podemos hacer con programación orientada a objetos
class Alumno:
    def __init__(self, nro_doc, nombre, apellido, edad):
        self.doc = nro_doc
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + self.apellido

    def estudiar(self):
        print("El alumno", self.nombre, "está estudiando.")

    def crecer(self):
        self.edad += 1
        print("El alumno:", self.nombre, "ahora tiene", self.edad, "años.")

alumno_1 = Alumno(456859485, "Luciana", "Fernandez", 20)
alumno_2 = Alumno(2341234, "nombre", "apellido generico", 67)
print(alumno_1)
alumno_1.estudiar()
print("Edad:", alumno_1.edad)
alumno_1.crecer()
alumno_1.crecer()
alumno_1.crecer()

# Ejercicio realizado en clase: Vehiculos

# Definicion de la clase vehiculo de la cual van a heredar todos los vehiculos
class Vehiculo:
    def __init__(self, marca, modelo, capacidad_combustible):
        self.marca = marca
        self.modelo = modelo
        self.capacidad_combustible = capacidad_combustible

    def __str__(self):
        return "Marca: " + self.marca + " Modelo: " + self.modelo

    def moverse(self):
        print("El vehículo de la marca", self.marca, "modelo", self.modelo, "está en movimiento")

# Esta clase esta diseñada solo para darle funcionalidades a los objetos de tipo embarcación
class MovimientosEmbarcacion:
    def virar_a_estribor(self):
        print("Esta embarcación esta virando a estribor!")
    def virar_a_babor(self):
        print("Esta embarcación esta virando a babor")

# ----------------- Definición de Vehiculos -----------------------
class Auto(Vehiculo):
    def __init__(self, marca, modelo, comb, color, nro_puertas):
        super().__init__(marca, modelo, comb)
        self.color = color
        self.puertas = nro_puertas

    def tocar_bocina(self):
        print("Este auto esta haciendo piiiii piiiiiiii!!")

class Lancha(Vehiculo, MovimientosEmbarcacion):
    def __init__(self, marca, modelo, comb, asientos, calado):
        super().__init__(marca, modelo, comb)
        self.nro_asientos = asientos
        self.calado = calado

#-------------------------------------------------------------------
# Creación de instancias de vehiculos
automovil_1 = Auto("Toyota", "Corola", 50, "Verde Musgo", 3)
automovil_2 = Auto("Audi", "A4", 50, "Azul espacial", 4)
lancha_1 = Lancha("Yamaha", "125", 100, 5, 1.5)

# Realizando pruebas sobre los vehiculos creados
print(automovil_1)
print(lancha_1)

automovil_2.moverse()
lancha_1.virar_a_babor()
lancha_1.virar_a_estribor()
automovil_1.tocar_bocina()

# Ejemplo de encapsulamiento utilizando de nuevo la clase Alumno que vimos más temprano
class Alumno:
    def __init__(self, nro_doc, nombre, apellido, edad):
        self.__documento = nro_doc
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def __str__(self):
        return self.nombre + " " + self.apellido

    def estudiar(self):
        print("El alumno", self.nombre, "está estudiando.")

    def crecer(self):
        self.edad += 1
        print("El alumno:", self.nombre, "ahora tiene", self.edad, "años.")

    def get_documento(self):
        print("El numero de documento es:", self.__documento)
        return self.__documento

    def set_documento(self, nuevo_nro_documento):
        self.__documento = nuevo_nro_documento

alumno_1 = Alumno(456859485, "Luciana", "Fernandez", 20)

print(alumno_1.edad)
print(alumno_1.nombre)
nro_documento = alumno_1.get_documento()
print(nro_documento)

alumno_1.set_documento(11111111111)
alumno_1.get_documento()