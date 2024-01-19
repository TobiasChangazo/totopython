#definir una variable con o sin argumentos

def saludo():
    print("Hola!")


# el return sirve para recibir y retornar valores

#retornar valores

def saludar_por_nombre():
    nombre = input("ingrese su nombre: ")
    saludo = "bienvenido {} al sistema".format(nombre)
    return saludo
print(saludar_por_nombre())

#recibir valores
def suma(a,b):
    return a+b
r = suma(5,5)

#return utilizando slicing 

def lista():
    return [1,2,3,4,5]
print(lista()[1:3])

#funciones recursivas

def cuenta_recursiva(numero):
    print(numero)
    numero-=1
    if numero>0:
        cuenta_recursiva(numero)
    else:
        print("despegue")
        print("fin de la funcion", numero)

#funciones integradas

#la funcion int() me devuelve si o si un numero entero

int(2.5)
# = 2
int("25")
# = 25
#la funcion float() me devuelve un numero a en decimales

float("3.4545495")
# = 3.4545495

#la funcion str() me devuelve un string

str(100)
# = '100'

#la funcion round() redondea el numero

round(2.5)
# = 2
round(2.6)
# = 3