from modelo_clientes.cliente import Cliente


cliente1 = Cliente("Juan", "Lopez", 28, "juan@example.com")
cliente1.agregar_producto_al_carrito("Lavarropas")
cliente1.agregar_producto_al_carrito("Bicicleta")
cliente1.realizar_compra()
cliente1.mostrar_informacion()

print(" ")

cliente2 = Cliente("Ana", "Fernandez", 26, "ana@example.com")
cliente2.agregar_producto_al_carrito("Lampara")
cliente2.agregar_producto_al_carrito("Mesa")
cliente2.realizar_compra()
cliente2.mostrar_informacion()

print(" ")

cliente3 = Cliente("Mariano", "Martinez", 39, "mariano@example.com")
cliente3.realizar_compra()
cliente3.mostrar_informacion()