class Cliente:
    def __init__(self, nombre, apellido, edad, correo):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.correo = correo
        self.carrito = []
        
    def __str__(self):
        return self.nombre + " " + self.apellido
    
    #carrito de compras del cliente
    def agregar_producto_al_carrito(self, producto):
        self.carrito.append(producto)
        
    #compras del cliente
    def realizar_compra(self):
        if len(self.carrito) == 0:
            print(f"{self.nombre}, Su carrito está vacío.")
        else:
            print(f"{self.nombre}, Has realizado una compra con los siguientes productos:")
            for producto in self.carrito:
                print(producto)
            self.carrito = []

    #informacion del cliente
    def mostrar_informacion(self):
        print("La informacion del cliente es: ")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Edad: {self.edad}")
        print(f"Correo: {self.correo}")