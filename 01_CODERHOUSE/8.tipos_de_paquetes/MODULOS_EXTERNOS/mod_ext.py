#nos permite manipular y controlar estructuras de datos de manera eficiente (collections)

from collections import namedtuple

pez = namedtuple("pez", ["nombre", "especie", "peso"])

pez1 = pez("juan", "payaso", 1)

print(pez)


#nos ayuda a hacer cuentas con disccionarios y listas (counter)

from collections import Counter
 
lista = [1,2,3,4,465,5,6,7,67,68,67,]

print(Counter(lista))


#obtener al fecha y hora de cuando creamos la instancia (datetime)

from datetime import datetime

dt = datetime.now

print(datetime.year)
print(datetime.month)
print(datetime.day)

#nos permite hacer calculos matematicos de manera sencilla (math)

#sacar raiz cuadrada

import math

x = math.sqrt(20)

#redondear al entero mas cercano

x = math.ceil(1.4) #=2
y = math.floor(1.4) #=1


#nos permite obtener valores al azar (random)

import random

print(random.randrange(0, 20))

