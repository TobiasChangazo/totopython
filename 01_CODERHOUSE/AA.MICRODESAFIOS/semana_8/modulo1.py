class alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota


    def __str__(self):
        return self.nombre + " " + self.nota

    def imprimir(self):
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")