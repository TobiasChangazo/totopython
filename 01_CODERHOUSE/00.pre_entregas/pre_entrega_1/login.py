base_de_datos_usuarios = {}

def registrar_usuario():
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    perfil_del_usuario = {
        'usuario': usuario,
        'contraseña': contraseña,
        'nombre': nombre,
        'apellido': apellido,
    }

    base_de_datos_usuarios[usuario] = perfil_del_usuario
    print("Usuario registrado con éxito.")

def iniciar_sesion():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in base_de_datos_usuarios:
        perfil_del_usuario = base_de_datos_usuarios[usuario]

        if perfil_del_usuario['contraseña'] == contraseña:
            print("Iniciaste sesión con éxito.!")
        else:
            print("Contraseña incorrecta. Inténtelo nuevamente.")
    else:
        print("Usuario no encontrado. Regístrese primero.")

def mis_datos():
    usuario = input("Ingrese su nombre de usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if usuario in base_de_datos_usuarios:
        perfil_del_usuario = base_de_datos_usuarios[usuario]

        if perfil_del_usuario['contraseña'] == contraseña:
            print(f"Nombre: {perfil_del_usuario['nombre']}")
            print(f"Apellido: {perfil_del_usuario['apellido']}")
        else:
            print("La contraseña ingresada no corresponde al usuario!")
    else:
        print("Usuario no encontrado. Regístrese primero.")


#Menu del programa
while True:
    print("-----------------Menú-----------------")
    print("1. Registrar un nuevo usuario")
    print("2. Iniciar sesión")
    print("3. Mis datos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        registrar_usuario()
    elif opcion == '2':
        iniciar_sesion()
    elif opcion == '3':
        mis_datos()
    elif opcion == '4':
        break
    else:
        print("Opción no válida. Inténtelo nuevamente.")