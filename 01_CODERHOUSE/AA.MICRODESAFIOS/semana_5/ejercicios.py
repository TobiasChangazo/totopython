nombre_ciudad = input("ingrese la ciudad de donde se encuentra: ")

def saludo_por_ciudad(nombre_ciudad):
    saludo = ("¡¡Hola, te damos la bienvenida a {}!").format(nombre_ciudad)
    return saludo

print(saludo_por_ciudad(nombre_ciudad))

# Primer ejercicio de funciones: función promedio()

def promedio(*args):
    print(args)
    return sum(args) / len(args)

resultado = promedio(8, 9, 14, 64)
print(resultado)

print(promedio(int(input("ingrese valores: "))))

# Ejercicio: encontrar cuál número es múltiplo del otro:

def es_multiplo_1(a,b):
  if a % b == 0:
      resultado = f"El nro {a} es multiplo de {b}"
  elif b % a == 0:
      resultado = f"El nro {b} es multiplo de {a}"
  else:
      resultado = f"¡El nro {a} no es multiplo de {b} ni vice versa!"
  return resultado

print(es_multiplo_1(int(input('ingrese el numero')), int(input('ingrese el numero'))))
print(es_multiplo_1(5, 4))
print(es_multiplo_1(10, 2))
print(es_multiplo_1(10, 10))

# Ejercicio: Años bisiestos.

def anio_bisiesto(anio):
    if type(anio) != int:
        print('El dato ingresado no es váldio')
        return False

    if anio % 400 == 0 or (anio %4 == 0 and anio % 100 != 0):
        print(f"el año {anio} es bisiesto")
    else:
        print(f"El año {anio} no es bisiesto")

anio_bisiesto(2012)
anio_bisiesto(2010)
anio_bisiesto(2000)
anio_bisiesto(1900)

# Recursividad: Crear una función para calcular recursivamente el factorial de un número.

# Ejemplo de factoriales de algunos números:

# 1! = 1

# 2! = 2 * 1 = 2 * 1! = 2

# 3! = 3 * 2 * 1 = 3 * 2! = 6

# 4! = 4 * 3 * 2 * 1 = 4 * 3! = 24

# 5! = 5 * 4 * 3 * 2 * 1 = 5 * 4! = 120

def factorial(numero):
    print('valor inicial', numero)
    if numero > 1:
        numero = numero * factorial(numero-1)
    print('valor final', numero)
    return numero

print(factorial(4))

