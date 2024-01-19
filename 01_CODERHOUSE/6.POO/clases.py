#definir una clase

class perro:
    pass #para que no tire error

perro1 = perro()

perro2 = perro()


#atributos de instancia

class perro:
    def __init__(nombre, raza):
        pass

perro1 = perro()

perro2 = perro()

# atributos de clase

class perro:

    especie = "Mamifero"
    def __init__(self, nombre, raza) -> None:
        # atributos de instacia
        self.nombre = nombre
        self.raza = raza

perro1 = perro("tom", "caniche" )

print(perro1.raza)
print(perro1.nombre)
print(perro1.especie)


# metodos

class perro:

    especie = "Mamifero"
    def __init__(self, nombre, raza) -> None:
        # atributos de instacia
        self.nombre = nombre
        self.raza = raza

    # metodo con argumento
    def ladrar(self):
        print("este perro acaba de ladrar")

    # metodo sin argumento
    def caminar(self, pasos):
        print(f"este perro acaba de caminar {pasos}")


perro1 = perro("tom", "caniche" )

print(f"su raza es:{perro1.raza}")
print(f"su nombre es: {perro1.nombre}")
print(f"su especie es: {perro1.especie}")

print(perro1.ladrar)
print(perro1.caminar(10))