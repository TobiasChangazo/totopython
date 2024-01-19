# Microdesafió de operadores y booleanos

expresiones = [
    not False,
    not 3 == 5,
    33/3 == 11 and 5 > 2,
    True or False,
    True*5 == 2.5*2 or 123 >= 23,
    12 > 7 and True < False
]

resultados = [
    True,
    True,
    True,
    True,
    True,
    False
]

#print(bool(33/3 == 11))

print(5 % 2)

contador = 0
contador += 1
print(contador)

print(16 // 7.5)

# Ejercicio de expresiones anidadas:
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))

cumple_condiciones = (nombre != "****") and (5 < edad < 20) and (4 <= len(nombre) < 8) and  (edad * 3 > 35)

if cumple_condiciones:
        print("se cumplen las condiciones")
else:
        print("no se cumplen las condiciones")
        

# Ejemplos demostración de condicionales:
if True:
    print(' hola mundo ')

if False:
    print(' esto lo va a ignorar ')

if False:
    print(' esto tambien lo va a ignorar ')
else:
    if True:
        print(" Esto esta en el 'else' ")

if False:
    print( ' Ignorado ')
elif True:
    print(' esto tambien esta ignorado ')
elif True:
    print(' esto sí se va a imprimir ')

if True:
    if False:
        print(' acá hay un false ')
    if True:
        print(' esto sí se imprime')
        
        
# Ejercicio: Crédito Bancario

edad = 20
antiguedad = 7
ingreso = 2600

ingreso_minimo = 2500
ingreso_minimo_sin_antiguedad = 4000

# Resolución 1:
if (edad >= 18 and antiguedad >= 3 and ingreso >= ingreso_minimo) or (edad >= 18 and not antiguedad >= 3 and ingreso >= ingreso_minimo_sin_antiguedad):
    print('El crédito ha sido aprobado!!')
else:
    print(' Crédito denegado. :(')
    
# Resolución 2 (más legible):
if edad >= 18 and antiguedad >= 3 and ingreso >= ingreso_minimo:
    print('apto credito')

elif edad >= 18 and ingreso >= ingreso_minimo_sin_antiguedad:
    print('apto credito')

else:
    print('credito no aprobado')
    
# Otra solución propuesta por los estudiantes en la clase:

edad = 25
antiguedad = 2
ingreso = 1500

# Por defecto el credito no esta aprobado.
aprobado = False

if edad >= 18:
    if antiguedad >= 3 and ingreso >= 2500:
        aprobado = True

    elif ingreso >= 4000:
        aprobado = True

#     else:
#         aprobado = False

# else:
#     aprobado = False


if aprobado:
    print('Credito aprobado!')
else:
    print('Credito denegado.')