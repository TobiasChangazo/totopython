#argumento por posicion 

def resta(a,b):
    return a-b

print(resta(10,5))
 # = 5
print(resta(5,10))
 # = -5

#argumento por nombre

def resta(a,b):
    return a-b

print(resta(a=10,b=5))
 # = 5
print(resta(b=5,a=10))
 # = 5


#llamada sin argumento

def resta(a=10,b=5):
    return a-b
print(resta())


#argumento por valor y referencia

def duplicar_numero(lista_de_numeros):
    for i,n in enumerate(lista_de_numeros):
            lista_de_numeros[i] *=2

lista = [1,2,3,4]
duplicar_numero(lista)
print(lista)

#argumentos ideterminados (*args y **kwargs)

def sumar(*args):
    return sum(*args)

print(sumar(1,2))
# = 3

def sumar(**kwargs):
     resultado = 0
     for clave, valor in kwargs.items():
          print(clave, '=', valor)
          resultado *=valor
          return resultado

print(sumar(a=10,b=10,c=3))