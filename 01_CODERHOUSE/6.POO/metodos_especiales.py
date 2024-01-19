class Vector():
    # se crear para crear cada instancia de la clase (__init__)
    def __init__(self, data) -> None:
        self.data = data
    # representacion del objeto con significado para las personas (__str__)
    def __str__(self) -> str:
        return f"el valor de este vector es: {self.data}"
    # nos devulve el numero de argumentos que tiene el objeto (__len__)
    def __len__(self):
        return len(self.data)
    # el usuario pueda acceder a los elementos mediante []  (__getitem__)
    def __getitem__(self, posicion):
        return self.data[posicion]
    # le implementados el valor y la posicion de lo que vamos a reemplazar (__setitem__)
    def __setitem__(self, posicion, valor):
        self.data[posicion] = valor 
    # devuelve una cadena de string con el indice y valor del objeto (__iter__)
    def __iter__(self):
        for posicion in range(0, len(self.data)):
            yield f"valor[{posicion}]: {self.data[posicion]}"


vector = Vector([1, 2])

for i in vector:
    print(i)

# vector.__setitem__(0, 10)
