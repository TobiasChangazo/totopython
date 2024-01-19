# nos permite no repetir el codigo varias veces

class animal: 
    def __init__(self, especie, edad) -> None:
         self.especie = especie
         self.edad = edad
    
    def hablar(self):
        pass

    def camianar(self):
        pass

    def describeme(self):
        print("soy un animal del tipo", type(self).__name__)


class perro(animal):
    def hablar(self):
        print("guau")

    def camianar(self):
        print("camina en 4 patas")

perro1 = perro("mamifero", 2)

perro1.describeme()
perro1.hablar()
perro1.camianar()