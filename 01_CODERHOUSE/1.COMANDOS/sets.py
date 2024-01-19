#los set se utilizan entre {}
 
mi_set = {1,2,3,4}

#agregar un iteam a un set

mi_set.add(5)

#agregar mas de un iteam a un set

mi_set.update([5,6,7,8])

#me va dar la cantidad de elementos del set

len(mi_set)

#remueve un elemento del set y si no existe no tira error

mi_set.discard(1)
mi_set.discard(9) #no va a dar error

#remueve un elemento del set y si no existe va a tirar error

mi_set.discard(1)
mi_set.remove(9) #va a dar error

#validar si el elemento que dijimos esta dentro del set

1 in mi_set

#borrar el set

mi_set.clear

#nos remueve un numero aleatorio dentro del set

mi_set.pop()

#nos devuelve una copia del set original

mi_set2 = mi_set.copy()

#comprueba si un set es distinto al otro

mi_set2 = {4,5,6,7,8}

mi_set.isdisjoint(mi_set2)

#comprueba si todos los elementos de un set estan dentro de otro set 

mi_set.issubset(mi_set2)

#comprueba si los elementos que le decimos estan dentro del set

mi_set.issubset({1,3})

#me devuelve la union entre dos sets

mi_set.union[5,6,7,8]

#me devuelve los valores q encuentre diferente del otro set

mi_set.difference(mi_set2)

#va a reescribir el set con los elementos diferentes

mi_set.difference_update({3,4,5,6})

#me va a dar los elementos que son identicos entre los dos sets

mi_set.intersection(mi_set2)

#me va a reemplazar el set original con uno nuevo con los elementos que son identicos entre los dos sets 

mi_set.intersection_update(mi_set2)