# Primero el código que usamos para explicar el tema de ciclos.

while True:
   print('Este mensaje.')

while False:
    print('Este mensaje nunca se va a imprimir.')

contador = 0

while contador != 5:
    print('Esto se va a imprimir')
    contador += 1

lista = [1, 2, 3, 4, 5]

nombres = ['uno', 'dos', 'tres', 'cuatro', 'cinco']

diccionario_numeros = dict(zip(nombres, lista))

print(diccionario_numeros)

for numero in diccionario_numeros.values():
    print('Este mensaje es el numero:', numero)

lista = [1, 2, 3, 4, 5]
limite = len(lista)
cursor = 0

while cursor != limite:
    print('Este es el mensaje numero:', lista[cursor])
    cursor += 1
    
    
    
# Solucion Microdesafio:
numero=int(input("Ingresa un numero impar:"))

while numero%2 != 1:
     numero=int(input("Ingresa un numero impar:"))
else:
  print("Bien hecho")
  
  
# Función para determinar paridad de un número sin usar %
def es_par(numero): # Así se define una función. Vamos a verlo bien a fondo en la próxima clase.
    return (numero & 1) == 0 # En esta línea el operador & representa un AND y realiza una operación BINARIA (el resto de la explicación en el video de la clase).

# Ejemplo de número binario:
1101(binario) = 13(decimal)

# Los números a la izquierda representan el valor en decimal de cada dígito binario (numeros a la derecha).
1: 1 # Lo que hace la línea antes mencionada es verificar este último bit, y partir de eso define si es par (termina en 0) o impar (termina en 1).
2: 0
4: 1
8: 1


# Ejercicio Calculadora:
numero_1 = int(input("elige el 1er numero: "))
numero_2 = int(input("elige el 2do numero: "))

while True:

    txt = input("elige una opcion, suma, resta, multiplicacion, o finalizar: ")
    if txt == "suma":
        print(numero_1 + numero_2)
    elif txt == "resta":
        print(numero_1 - numero_2)
    elif txt == "multiplicacion":
        print(numero_1 * numero_2)
    elif txt == "finalizar":
        break
    else:
        print("esa opcion no es valida")
        
        
# Otra opcion
# En esta versión cambia un poco la interpretación del ejercicio. En lugar de ejecutar la calculadora indefinidas veces,
# solo se repite hasta que se realiza una operación correctamente.

numero1 = int(input("escriba su primer numero,  "))
numero2 = int(input("escriba su segundo numero,  "))
opcion_de_cuenta = int(input("escriba 0 para sumar, 1 para restar, 2 para multiplicar, 3 para finalizar el programa, "))

while True:
    if opcion_de_cuenta == 0:
        print(numero1 + numero2)
        break
    elif opcion_de_cuenta == 1:
        print(numero1 - numero2)
        break
    elif opcion_de_cuenta == 2:
        print(numero1 * numero2)
        break
    elif opcion_de_cuenta == 3:
        print("programa finalizado")
        break
    else:
        print("opcion no valida")
        opcion_de_cuenta = int(input("escriba 0 para sumar, 1 para restar, 2 para multiplicar, 3 para finalizar el programa, "))
        
# Otra solución más propuesta por un estudiante.
# Esta es muy parecida a la primera, pero en lugar de iniciar con while True y usar un break dentro de un condicional, utiliza una
# variable que cambia dentro del ciclo para romper el ciclo.

numero1= int(input('Elija el primer numero: '))
numero2= int(input('Elija el segundo numero: '))

print("""
     Opcion 1 - Mostrar suma de los numeros,
     Opcion 2 - Mostrar resta de los numeros,
     Opcion 3 - Mostrar multiplicacion de los numeros,
     Opcion 4 - Finalizar programa""")

print('')


opciones= 0

while opciones !='4':
    opciones = input('Elija una opcion: ')
    if opciones == '1':
        print(numero1 + numero2)
    elif opciones == '2':
        print(numero1 - numero2)
    elif opciones == '3':
        print(numero1 * numero2)
    elif opciones == '4':
        print('Programa Finalizado')
    else:
        print('Esa opcion no existe')


# Ejercicio: La Media

cantidad_de_numeros = int(input("Cuántos números quiere introducir?: "))

lista = []

for i in range(cantidad_de_numeros):
    numero = int(input("Ingrese el numero: "))
    lista.append(numero)

print("Lista de numeros: ", lista)

promedio = sum(lista) / len(lista)

print("El promedio de los numeros ingresados es:", promedio)


# Ejercicio con enumerate:

# Por medio de enumerate le asignamos una numeración a las frutas de un diccionario y las guardamos en una lista de tuplas para
# no olvidar el código asignado.

stock_de_frutas = {'banana': 567, 'anana': 363, 'naranja': 123, 'manzana': 435, 'mango': 345}

lista_frutas = []

for indice, fruta in enumerate(stock_de_frutas):
    lista_frutas.append((indice, fruta, stock_de_frutas[fruta]))

print(lista_frutas)

# Ahora voy a agregar más frutas a la lista, pero para seguir numerandolas empezar a contar a donde nos quedamos antes.

stock_de_frutas_2 = {'sandía': 345, 'durazno':127, 'frutilla': 900, 'pera': 341}

# enumerate puede tomar dos datos: enumerate(iterable, inicio). El inicio es el número a partir del cual
# empieza a contar. En este caso, quiero que la numeración continúe donde terminó el conteo anterior, para eso utilizo el largo
# de la lista actual

inicio = len(lista_frutas)

for indice, fruta in enumerate(stock_de_frutas_2, inicio):
    lista_frutas.append((indice, fruta, stock_de_frutas_2[fruta]))

print(lista_frutas)


# Ejemplo de fstrings y format

lista = [1, 2, 3, 4, 5]

print(f'La sumatoria de la lista es: {sum(lista)}, el promedio es: {sum(lista)/len(lista)}')

print('Sumatoria: {}, promedio: {}'.format(sum(lista), sum(lista)/len(lista)))