mi_variable = "como estan"
otra_variable = "hola mundo"
numeros = [1,2,3,4]
#Listas son entre [ ]

mi_lista = [mi_variable, otra_variable]
otra_lista = ["rojo", "perro", 10]
print(mi_lista + otra_lista)

#acceder a algo en especifico dentro de la lista.  se cuenta desde el 0 en adelante
mi_lista[3] #accedo al indice numero 4 de la lista
mi_lista[3][1] #accedo al indice numero 2 dentro de la lista
mi_lista[3][1][0] #accedo a la primera palabra del elemento seleccionado
mi_lista[2] = 20 #reemplaza el indice numero 3 por el 20

#agregar algo a la lista

mi_lista.append("hola")
mi_lista.append(otra_lista)

#saber la cantidad de elementos de la lista

len(mi_lista)

#extrae el ultimo valor de la lista

numeros.pop()

#define cuantas veces se repite un mismo elemento en una lista

numeros.count(2)

#nos da el lugar donde se encuentra el elemento que elijamos dentro de la lista

numeros.index(2)

#borrar mi lista

numeros.clear

#nos permite extender la lista sin tener usar el +

numeros.extend([5,6,7])

#nos permite añadir un elemento en una determina pocición

numeros.insert(0,0)

#agregar un elemento en la ultima posición de la lista

n = len(numeros)

numeros.insert(n, 5)

#nos permite revertir el orden dentro de la lista

numeros.reverse()

#nos permite ordenar de menor a mayor los numeros dentro de la lista

numeros.sort()

#nos permite ordenar de mayor a menor los numeros dentro de la lista

numeros.sort(reverse=True)