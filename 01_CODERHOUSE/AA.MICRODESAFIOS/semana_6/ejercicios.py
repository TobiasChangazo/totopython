# Microdesafío

def dividir(a, b):
    if b == 0:
        return None
    return a / b

print(dividir(34, 0))
print(dividir(7, 2))

def dividir_2(a, b):
    try:
        return a / b
    except Exception as error:
        print("La operación no se pudo completar porque: ", error)


print(dividir_2(34, 0))
print(dividir_2(7, 2))

# Volvemos a trabajar con el Microdesafío pero probando otras posibilidades de try-except
def dividir(a, b):
    try:
        resultado = c # Esta linea va a forzar la excepción NameError
        return a / b
    except ZeroDivisionError:
        print("La operación no se pudo completar porque hay una división por cero.")
    except TypeError:
        print("Hubo un error en los tipos de dato.")
    except NameError:
        print("El argumento apunta a una variable intexistente.")
    except Exception as e:
        print("La operacion no se pudo completar porque: ")

print(dividir(67, 23))
print(dividir(67, 0))
print(dividir(67, (45, 'asdf')))

# Una opción alternativa de resolver el ejercicio "Año Bisiesto" de la clase pasada.

def anio_bisiesto():
    try:
        anio = int(input('Ingrese el año: '))
    except:
        print("No se ingreso un dato valido.")
        return None

    if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
            print(f"el año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

print(anio_bisiesto())

# Ejercicio: "Generar el error"

def menu():
    print("Selecciona una opción:")
    print("1. 'Soy un string' - TypeError")
    print("2. 4/0 - ZeroDivisionError")
    print("3. prnt('Mostrando código') - NameError")
    print("4. int('Quiero ser un número') - ValueError")

    opcion = input("Ingrese el número de opción: ")

    if opcion == '1':
        try:
            resultado = 'Soy un string' - 4
        except TypeError as e:
            print(f"Error: {e}")

    elif opcion == '2':
        try:
            resultado = 4 / 0
        except ZeroDivisionError as e:
            print(f"Error: {e}")

    elif opcion == '3':
        try:
            prnt('Mostrando código')
        except NameError as e:
            print(f"Error: {e}")

    elif opcion == '4':
        try:
            resultado = int('Quiero ser un número')
        except ValueError as e:
            print(f"Error: {e}")

    else:
        print("Opción no válida")

print(menu())


# Usamos las sentencias else y finally en un ejercicio ya conocido

def anio_bisiesto():
    try:
        anio = int(input('Ingrese el año: '))
    except:
        print("No se ingreso un dato valido.")
        return None
    else:
        print("El dato es válido.")
    finally:
        print('Esta linea se deberia ejecutar siempre')

    if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
            print(f"el año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

print(anio_bisiesto())

