# lista_numeros = []

# def promedio_numeros(cantidad_de_numeros):

#     for i in range(cantidad_de_numeros):
#         numero = int(input("ingrese numero:"))
#         lista_numeros.append(numero)
#         promedio = sum(lista_numeros) / cantidad_de_numeros

#     return promedio

# cantidad_de_numeros = int(input("cuantos numeros quiere introducir?: ")) #para añadir cantidad numeros especificos
# print(promedio_numeros(cantidad_de_numeros))


# def es_multiplo (a,b):
#   if a % b == 0:
#       resultado = f"El nro {a} es multiplo de {b}"
#   elif b % a == 0:
#       resultado = f"El nro {b} es multiplo de {a}"
#   else:
#       resultado = f"¡El nro {a} no es multiplo de {b} ni vice versa!"
#   return resultado

# def es_multiplo():
#     numero1= int(input("Ingrese el Primer Numero: "))
#     numero2= int(input("Ingrese el Segundo Nuemero: "))
    
    
#     if numero1 % numero2 == 0 or numero2 % numero1 ==0:
#         print ("Los numeros son multiplos")
#     else: print ("No son multiplos") 

#     return es_multiplo

# print(es_multiplo())

# class vehiculo():
#     def __init__(self, color, anio) -> None:
#         self.color = color
#         self.anio = anio 

#     def marca(self):
#         pass

# class Auto(vehiculo):
#     def marca(self):
#         print("la marca del auto es toyota")

# auto = Auto("rojo", 2014)

# auto.marca()
# print(f"el color del auto es: {auto.color}")
# print(f"el anio del auto es: {auto.anio}")




# class electrodomesticos:

#     def __init__(self,precio_base=100,color="blanco",consumo_energetico="F",peso=5):
#         self.precio_base = precio_base
#         self.color = color
#         self.consumo_energetico = consumo_energetico
#         self.peso = peso

#     def comprobar_consumo(self,letra):
#         lista_consumo = ["A", "B", "C", "D", "E", "F"]

#         if letra.upper() in lista_consumo:
#             return letra.upper()
#         else:
#             return "F"

#     def comprobar_color(self,color):
#         colores_disponibles = ["blanco","negro","rojo","azul","gris"]

#         if color.lower() in colores_disponibles:
#             return color.lower()
#         else:
#             return "blanco"

#     def precio_final(self):
#         precio = self.precio_base

#         if self.consumo_energetico == "A":
#             precio += 100
#         elif self.consumo_energetico == "B":
#             precio += 80
#         elif self.consumo_energetico == "C":
#             precio += 60
#         elif self.consumo_energetico == "D":
#             precio += 50
#         elif self.consumo_energetico == "E":
#             precio += 30
#         elif self.consumo_energetico == "F":
#             precio += 10

#         if 0 < self.peso < 19:
#             precio += 10
#         elif 20 < self.peso < 49:
#             precio += 50
#         elif 50 < self.peso < 79:
#             precio += 80
#         elif 80 < self.peso:
#             precio += 100

#         return precio

# #precios cambiables
# electrodomestico1 = electrodomesticos(precio_base=500,color="rojo",consumo_energetico="A",peso=5)
# print(f"precio televisor sin tener en cuenta pulgadas y sitonizador: {electrodomestico1.precio_final()}")

# #variable para implementar en la funcion de la clase hija "televisor".
# precio = electrodomestico1.precio_final()
# #la idea es que agarre todo desde la padre hija y que se le pueda cambiar la resolucion o el sintonizador y sino que el programa agarre las ya definidas.

# class televisor(electrodomesticos):
#     def __init__(self,precio_base,color,consumo_energetico,peso, resolucion=float(20),sintonizador_TDT=False):
#         super().__init__(precio_base,color,consumo_energetico,peso)
#         self.resolucion = resolucion
#         self.sintonizador_TDT = sintonizador_TDT

#     def precio_final(self,precio): # ?????? como hago para hacer que repita el codigo de arriba, sin tener que volver a codearlo
#         precio_nuevo = precio

#         if self.resolucion > float(40):
#             precio_nuevo *= (1+0.30)

#         if self.sintonizador_TDT == True:
#             precio_nuevo += 50

#         return precio_nuevo

# televisor6 = televisor(precio_base=0,color="",consumo_energetico="",peso=0,resolucion=float(45),sintonizador_TDT=True)
# print(f"el precio final del televisor es: {televisor6.precio_final(precio)}")
# print("")
# print(televisor.__mro__)

# televisor7 = televisor(precio_base=0,color="",consumo_energetico="",peso=0)
# print(f"el precio final del televisor es: {televisor7.precio_final(precio)}")





# class Persona:
#     def __init__(self, nombre, edad, email, direccion):
#         self.__nombre = nombre
#         self.__edad = edad
#         self.__email = email
#         self.__direccion = direccion

#     def get_edad(self):
#         print("La edad es de: ", self.__edad)

#     def set_edad(self, edad):
#         self.__edad = edad

#     def get_info(self):
#         print(self.__nombre, ":")
#         print("Edad: ", self.__edad)
#         print("Email: ", self.__email)
#         print("Dirección: ", self.__direccion)

# class Materia:
#     def __init__(self, nombre, division, facultad):
#         self.nombre = nombre
#         self.division = division
#         self.facultad = facultad

# class Alumno(Persona):
#     def __init__(self, nombre, edad, email, direccion, num_estudiante):
#         super().__init__(nombre, edad, email, direccion)
#         self.num_estudiante = num_estudiante
#         self.materias_matriculadas = []

#     def añadir_materia(self, materia):
#         self.materias_matriculadas.append(materia)
    
#     def sacar_materia(self, materia):
#         self.materias_matriculadas.remove(materia)
    
#     def materias_cursadas(self):
#         print("Las materias que cursa son: ", [m.nombre for m in self.materias_matriculadas])

# class Profesor(Persona):
#     def __init__(self, nombre, edad, email, direccion, num_empleado):
#         super().__init__(nombre, edad, email, direccion)
#         self.num_empleado = num_empleado
#         self.materias_prof = []

#     def añadir_materia(self, materia):
#         self.materias_prof.append(materia)

#     def sacar_materia(self, materia):
#         self.materias_prof.remove(materia)

# # Clase principal para gestionar alumnos, profesores, materias, etc.
# class Escuela:
#     def __init__(self):
#         self.alumnos = []
#         self.profesores = []
#         self.materias = []

#     def agregar_alumno(self, alumno):
#         self.alumnos.append(alumno)

#     def agregar_profesor(self, profesor):
#         self.profesores.append(profesor)

#     def agregar_materia(self, materia):
#         self.materias.append(materia)

#     def mostrar_info(self):
#         print("Alumnos:")
#         for alumno in self.alumnos:
#             print(alumno.get_info())
#         print("\nProfesores:")
#         for profesor in self.profesores:
#             print(profesor.get_info())
#         print("\nMaterias:")
#         for materia in self.materias:
#             print(materia.get_info())

# # Crear instancias de la clase Escuela y agregar alumnos, profesores y materias
# escuela = Escuela()

# alumno1 = Alumno("Juan Pérez", 20, "juan@example.com", "Calle 123", 12345)
# alumno2 = Alumno("María García", 22, "maria@example.com", "Calle 456", 67890)

# materia1 = Materia("Matemáticas", "A", "Facultad de Ciencias")
# materia2 = Materia("Historia", "B", "Facultad de Humanidades")

# profesor1 = Profesor("Carlos López", 40, "carlos@example.com", "Calle 789", 9876)
# profesor2 = Profesor("Ana Rodríguez", 35, "ana@example.com", "Calle 321", 5432)

# alumno1.añadir_materia(materia1)
# alumno2.añadir_materia(materia2)

# profesor1.añadir_materia(materia1)
# profesor2.añadir_materia(materia2)

# escuela.agregar_alumno(alumno1)
# escuela.agregar_alumno(alumno2)
# escuela.agregar_profesor(profesor1)
# escuela.agregar_profesor(profesor2)
# escuela.agregar_materia(materia1)
# escuela.agregar_materia(materia2)

# # Mostrar la información de la escuela
# escuela.mostrar_info()

